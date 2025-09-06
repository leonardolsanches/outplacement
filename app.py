from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'outplacement-platform-secret-key'
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
app.config['SESSION_PERMANENT'] = False

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'
login_manager.login_message_category = 'info'

# Arquivos de dados JSON
DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

USERS_FILE = os.path.join(DATA_DIR, 'users.json')
EXECUTIVES_FILE = os.path.join(DATA_DIR, 'executives.json')
SESSIONS_FILE = os.path.join(DATA_DIR, 'sessions.json')
REPORTS_FILE = os.path.join(DATA_DIR, 'reports.json')
KPIS_FILE = os.path.join(DATA_DIR, 'kpis.json')

# Inicializar arquivos JSON se não existirem
def init_json_files():
    files = {
        USERS_FILE: [],
        EXECUTIVES_FILE: [],
        SESSIONS_FILE: [],
        REPORTS_FILE: [],
        KPIS_FILE: {}
    }
    
    for file_path, default_data in files.items():
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump(default_data, f, indent=2)

# Classe do usuário para Flask-Login
class User(UserMixin):
    def __init__(self, user_id, username, email, role):
        self.id = user_id
        self.username = username
        self.email = email
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)
    
    for user in users:
        if user['id'] == user_id:
            return User(user['id'], user['username'], user['email'], user['role'])
    return None

# Funções auxiliares para dados JSON
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

# Rotas principais
@app.route('/')
def index():
    # Acesso direto ao dashboard sem login
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        print(f"DEBUG: Tentativa de login - Usuário: {username}")
        
        if not username or not password:
            print("DEBUG: Campos vazios")
            flash('Por favor, preencha todos os campos')
            return render_template('login.html')
        
        try:
            users = load_json(USERS_FILE)
            print(f"DEBUG: Total de usuários no sistema: {len(users)}")
            
            for user in users:
                print(f"DEBUG: Verificando usuário: {user['username']}")
                if user['username'] == username:
                    print("DEBUG: Usuário encontrado, verificando senha...")
                    if check_password_hash(user['password'], password):
                        print("DEBUG: Senha correta, fazendo login...")
                        user_obj = User(user['id'], user['username'], user['email'], user['role'])
                        login_success = login_user(user_obj, remember=True)
                        print(f"DEBUG: Login user result: {login_success}")
                        
                        # Verificar se o login foi bem-sucedido
                        if login_success:
                            print(f"DEBUG: Login bem-sucedido! User authenticated: {current_user.is_authenticated}")
                            print(f"DEBUG: Current user ID: {current_user.id}")
                            print(f"DEBUG: Session info: {dict(session)}")
                            
                            # Forçar commit da sessão
                            session.permanent = True
                            
                            # Usar next parameter se disponível, senão dashboard
                            next_page = request.args.get('next')
                            if next_page:
                                print(f"DEBUG: Redirecionando para next: {next_page}")
                                return redirect(next_page)
                            else:
                                print("DEBUG: Redirecionando para dashboard...")
                                dashboard_url = url_for('dashboard')
                                print(f"DEBUG: URL do dashboard: {dashboard_url}")
                                return redirect(dashboard_url)
                        else:
                            print("DEBUG: Falha no login_user()")
                            flash('Erro interno no sistema de login')
                            return render_template('login.html')
                    else:
                        print("DEBUG: Senha incorreta")
                        flash('Senha incorreta')
                        return render_template('login.html')
            
            print("DEBUG: Usuário não encontrado na base de dados")
            flash('Usuário não encontrado')
        except Exception as e:
            print(f"DEBUG: Erro durante login: {str(e)}")
            flash(f'Erro no sistema: {str(e)}')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/auth-test')
def auth_test():
    """Endpoint para testar status de autenticação"""
    return {
        'authenticated': current_user.is_authenticated,
        'user_id': current_user.id if current_user.is_authenticated else None,
        'username': current_user.username if current_user.is_authenticated else None,
        'session': dict(session)
    }

@app.route('/dashboard')
def dashboard():
    print("DEBUG: Dashboard acessado (modo sem login)")
    
    try:
        # Carregar dados para o dashboard
        executives = load_json(EXECUTIVES_FILE)
        sessions = load_json(SESSIONS_FILE)
        kpis = load_json(KPIS_FILE)
        
        print(f"DEBUG: Carregados {len(executives)} executivos, {len(sessions)} sessões")
        
        # Mostrar todos os dados (acesso livre sem login)
        # Sem filtros de usuário
        
        print("DEBUG: Renderizando template dashboard.html")
        return render_template('dashboard.html', 
                             executives=executives, 
                             sessions=sessions, 
                             kpis=kpis)
    except Exception as e:
        print(f"DEBUG: Erro no dashboard: {str(e)}")
        flash(f'Erro ao carregar dashboard: {str(e)}')
        return render_template('dashboard.html', 
                             executives=[], 
                             sessions=[], 
                             kpis={})

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        
        users = load_json(USERS_FILE)
        
        # Verificar se usuário já existe
        for user in users:
            if user['username'] == username or user['email'] == email:
                flash('Usuário já existe')
                return render_template('register.html')
        
        # Criar novo usuário
        new_user = {
            'id': str(uuid.uuid4()),
            'username': username,
            'email': email,
            'password': generate_password_hash(password),
            'role': role,
            'created_at': datetime.now().isoformat()
        }
        
        users.append(new_user)
        save_json(USERS_FILE, users)
        
        flash('Conta criada com sucesso! Faça login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# API endpoints
@app.route('/api/executives', methods=['GET', 'POST'])
def api_executives():
    if request.method == 'POST':
        data = request.json or {}
        executives = load_json(EXECUTIVES_FILE)
        
        new_executive = {
            'id': str(uuid.uuid4()),
            'name': data.get('name', ''),
            'email': data.get('email', ''),
            'phone': data.get('phone', ''),
            'company': data.get('company', ''),
            'position': data.get('position', ''),
            'start_date': datetime.now().isoformat(),
            'status': 'active',
            'consultant_id': data.get('consultant_id', 'admin'),
            'created_at': datetime.now().isoformat()
        }
        
        executives.append(new_executive)
        save_json(EXECUTIVES_FILE, executives)
        
        return jsonify({'success': True, 'id': new_executive['id']})
    
    # GET
    executives = load_json(EXECUTIVES_FILE)
    # Mostrar todos os executivos (modo sem login)
    
    return jsonify(executives)

# Rotas para Diagnóstico e Perfil Profissional
@app.route('/profile/<executive_id>')
def executive_profile(executive_id):
    executives = load_json(EXECUTIVES_FILE)
    executive = next((e for e in executives if e['id'] == executive_id), None)
    
    if not executive:
        flash('Executivo não encontrado')
        return redirect(url_for('dashboard'))
    
    # Carregar dados de perfil se existirem
    profiles_file = os.path.join(DATA_DIR, 'profiles.json')
    if not os.path.exists(profiles_file):
        with open(profiles_file, 'w') as f:
            json.dump([], f)
    
    profiles = load_json(profiles_file)
    profile = next((p for p in profiles if p['executive_id'] == executive_id), None)
    
    return render_template('profile.html', executive=executive, profile=profile)

@app.route('/api/profile', methods=['POST'])
def save_profile():
    data = request.json or {}
    profiles_file = os.path.join(DATA_DIR, 'profiles.json')
    
    if not os.path.exists(profiles_file):
        with open(profiles_file, 'w') as f:
            json.dump([], f)
    
    profiles = load_json(profiles_file)
    
    # Encontrar perfil existente ou criar novo
    profile_index = next((i for i, p in enumerate(profiles) if p['executive_id'] == data.get('executive_id')), None)
    
    profile_data = {
        'executive_id': data.get('executive_id'),
        'strengths': data.get('strengths', []),
        'competencies': data.get('competencies', []),
        'career_goals': data.get('career_goals', ''),
        'preferred_industries': data.get('preferred_industries', []),
        'salary_expectation': data.get('salary_expectation', ''),
        'linkedin_profile': data.get('linkedin_profile', ''),
        'updated_at': datetime.now().isoformat()
    }
    
    if profile_index is not None:
        profiles[profile_index] = profile_data
    else:
        profiles.append(profile_data)
    
    save_json(profiles_file, profiles)
    return jsonify({'success': True})

# Rotas para Agendamento de Sessões
@app.route('/schedule/<executive_id>')
def schedule_session(executive_id):
    executives = load_json(EXECUTIVES_FILE)
    executive = next((e for e in executives if e['id'] == executive_id), None)
    
    if not executive:
        flash('Executivo não encontrado')
        return redirect(url_for('dashboard'))
    
    sessions = load_json(SESSIONS_FILE)
    executive_sessions = [s for s in sessions if s.get('executive_id') == executive_id]
    
    return render_template('schedule.html', executive=executive, sessions=executive_sessions)

@app.route('/api/sessions', methods=['GET', 'POST'])
def api_sessions():
    if request.method == 'POST':
        data = request.json or {}
        sessions = load_json(SESSIONS_FILE)
        
        new_session = {
            'id': str(uuid.uuid4()),
            'executive_id': data.get('executive_id'),
            'consultant_id': 'admin',
            'date': data.get('date'),
            'time': data.get('time'),
            'type': data.get('type', 'individual'),
            'status': 'scheduled',
            'notes': data.get('notes', ''),
            'created_at': datetime.now().isoformat()
        }
        
        sessions.append(new_session)
        save_json(SESSIONS_FILE, sessions)
        
        return jsonify({'success': True, 'id': new_session['id']})
    
    # GET
    sessions = load_json(SESSIONS_FILE)
    # Mostrar todas as sessões (modo sem login)
    
    return jsonify(sessions)

# Simulador de Entrevistas
@app.route('/interview-simulator/<executive_id>')
def interview_simulator(executive_id):
    executives = load_json(EXECUTIVES_FILE)
    executive = next((e for e in executives if e['id'] == executive_id), None)
    
    if not executive:
        flash('Executivo não encontrado')
        return redirect(url_for('dashboard'))
    
    # Perguntas de exemplo para diferentes tipos de entrevista
    interview_questions = {
        'behavioral': [
            'Conte-me sobre uma situação em que você teve que liderar uma equipe em um projeto desafiador.',
            'Descreva um momento em que você teve que tomar uma decisão difícil rapidamente.',
            'Como você lida com conflitos em equipe?',
            'Qual foi seu maior fracasso profissional e o que aprendeu com ele?'
        ],
        'technical': [
            'Quais são suas principais competências técnicas?',
            'Como você se mantém atualizado com as tendências do seu setor?',
            'Descreva um projeto complexo que você liderou do início ao fim.',
            'Qual metodologia você prefere para gerenciar projetos?'
        ],
        'leadership': [
            'Como você motivaria uma equipe desmotivada?',
            'Qual é seu estilo de liderança?',
            'Como você desenvolveria o potencial de seus subordinados?',
            'Conte sobre uma situação em que teve que implementar mudanças organizacionais.'
        ]
    }
    
    return render_template('interview_simulator.html', 
                         executive=executive, 
                         questions=interview_questions)

# Relatórios e KPIs
@app.route('/reports')
def reports():
    # Calcular KPIs
    executives = load_json(EXECUTIVES_FILE)
    sessions = load_json(SESSIONS_FILE)
    
    # KPI 1: Taxa de recolocação
    total_executives = len(executives)
    recolocated = len([e for e in executives if e.get('status') == 'recolocated'])
    recolocation_rate = (recolocated / total_executives * 100) if total_executives > 0 else 0
    
    # KPI 2: Tempo médio de resposta
    response_times = []  # Implementação futura
    avg_response_time = 0.8  # Placeholder
    
    # KPI 3: Satisfação média
    satisfaction_scores = []  # Implementação futura
    avg_satisfaction = 85  # Placeholder
    
    # KPI 4: Sessões por mês
    current_month_sessions = len([s for s in sessions 
                                if datetime.fromisoformat(s['created_at']).month == datetime.now().month])
    
    kpis = {
        'total_executives': total_executives,
        'recolocation_rate': recolocation_rate,
        'avg_response_time': avg_response_time,
        'avg_satisfaction': avg_satisfaction,
        'monthly_sessions': current_month_sessions,
        'sla_compliance': {
            'response_time': 95,
            'program_start': 88,
            'monthly_sessions': 92,
            'monthly_reports': 100
        }
    }
    
    return render_template('reports.html', kpis=kpis)

@app.route('/api/reports/export')
def export_report():
    # Gerar relatório em JSON
    executives = load_json(EXECUTIVES_FILE)
    sessions = load_json(SESSIONS_FILE)
    
    report_data = {
        'generated_at': datetime.now().isoformat(),
        'total_executives': len(executives),
        'total_sessions': len(sessions),
        'executives': executives,
        'sessions': sessions
    }
    
    return jsonify(report_data)

if __name__ == '__main__':
    init_json_files()
    # Criar usuário admin padrão se não existir
    users = load_json(USERS_FILE)
    
    print(f"DEBUG: Arquivo de usuários carregado com {len(users)} usuários")
    
    # Verificar se existe usuário admin
    admin_exists = any(user['username'] == 'admin' for user in users)
    
    if not admin_exists:
        admin_user = {
            'id': str(uuid.uuid4()),
            'username': 'admin',
            'email': 'admin@outplacement.com',
            'password': generate_password_hash('admin123'),
            'role': 'admin',
            'created_at': datetime.now().isoformat()
        }
        users.append(admin_user)
        save_json(USERS_FILE, users)
        print("DEBUG: Usuário admin criado com credenciais: admin/admin123")
        print(f"DEBUG: Hash da senha: {admin_user['password']}")
    else:
        print("DEBUG: Usuário admin já existe")
        # Verificar se a senha do admin está correta
        admin_user = next(user for user in users if user['username'] == 'admin')
        print(f"DEBUG: Hash da senha do admin: {admin_user['password']}")
        # Testar se a senha está funcionando
        test_result = check_password_hash(admin_user['password'], 'admin123')
        print(f"DEBUG: Teste da senha admin123: {test_result}")
    
    app.run(host='0.0.0.0', port=5000, debug=True)