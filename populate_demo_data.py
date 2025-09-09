import json
import uuid
from datetime import datetime, timedelta
import random

# Executivos simulados com diferentes progressos nas 5 fases
demo_executives = [
    {
        "id": str(uuid.uuid4()),
        "name": "Carlos Silva",
        "email": "carlos.silva@email.com",
        "phone": "(11) 99999-1234",
        "company": "Tech Solutions Ltda",
        "position": "Diretor de TI",
        "level": "executivo",
        "start_date": (datetime.now() - timedelta(days=45)).isoformat(),
        "status": "active",
        "consultant_id": "admin",
        "created_at": (datetime.now() - timedelta(days=45)).isoformat(),
        "current_phase": 3,
        "overall_progress": 65,
        "phases": {
            "1": {
                "name": "Acolhimento & Diagnóstico",
                "description": "Acolhimento emocional, diagnóstico 360° e plano de ação individual",
                "status": "completed",
                "progress": 100,
                "start_date": (datetime.now() - timedelta(days=45)).isoformat(),
                "end_date": (datetime.now() - timedelta(days=35)).isoformat(),
                "activities": {
                    "acolhimento_emocional": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=42)).isoformat(),
                        "notes": "Sessão muito produtiva, executivo demonstrou boa disposição para mudanças"
                    },
                    "diagnostico_360": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=40)).isoformat(),
                        "notes": "Perfil forte em liderança técnica, oportunidades em gestão de pessoas"
                    },
                    "plano_acao_individual": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=35)).isoformat(),
                        "notes": "Plano focado em posições de CTO em empresas de médio/grande porte"
                    }
                }
            },
            "2": {
                "name": "Narrativa & Marca Pessoal",
                "description": "Construção de narrativa, marca pessoal e pitch de apresentação",
                "status": "completed",
                "progress": 100,
                "start_date": (datetime.now() - timedelta(days=35)).isoformat(),
                "end_date": (datetime.now() - timedelta(days=20)).isoformat(),
                "activities": {
                    "narrativa_marca_pessoal": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=30)).isoformat(),
                        "notes": "Currículo reformulado com foco em transformação digital"
                    },
                    "pitch_apresentacao": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=25)).isoformat(),
                        "notes": "Pitch de 30 segundos e 2 minutos prontos e treinados"
                    },
                    "oratoria_visibilidade": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=20)).isoformat(),
                        "notes": "Participação em webinar sobre inovação tecnológica"
                    }
                }
            },
            "3": {
                "name": "Preparação para o Mercado",
                "description": "ReSkilling, UpSkilling e preparação para entrevistas",
                "status": "in_progress",
                "progress": 67,
                "start_date": (datetime.now() - timedelta(days=20)).isoformat(),
                "end_date": None,
                "activities": {
                    "reskilling_upskilling": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=15)).isoformat(),
                        "notes": "Curso de Cloud Computing AWS concluído com certificação"
                    },
                    "simulacoes_entrevistas": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=10)).isoformat(),
                        "notes": "4 simulações realizadas, melhoria significativa na comunicação"
                    },
                    "relatorio_prontidao": {
                        "completed": False,
                        "date": None,
                        "notes": "Agendado para próxima semana"
                    }
                }
            },
            "4": {
                "name": "Conexão com o Mercado",
                "description": "Mentorias, busca ativa e rede de conexões",
                "status": "pending",
                "progress": 0,
                "start_date": None,
                "end_date": None,
                "activities": {
                    "mentorias_profissionais": {"completed": False, "date": None, "notes": ""},
                    "busca_ativa_posicoes": {"completed": False, "date": None, "notes": ""},
                    "rede_conexoes": {"completed": False, "date": None, "notes": ""},
                    "arenas_visibilidade": {"completed": False, "date": None, "notes": ""}
                }
            },
            "5": {
                "name": "Acompanhamento & Consolidação",
                "description": "Relatórios de progresso e dossiê final de transição",
                "status": "pending",
                "progress": 0,
                "start_date": None,
                "end_date": None,
                "activities": {
                    "relatorios_digitais": {"completed": False, "date": None, "notes": ""},
                    "indicadores_progresso": {"completed": False, "date": None, "notes": ""},
                    "dossie_final": {"completed": False, "date": None, "notes": ""}
                }
            }
        }
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Ana Paula Santos",
        "email": "ana.santos@email.com",
        "phone": "(11) 98888-5678",
        "company": "Banco Regional S.A.",
        "position": "Gerente Executiva",
        "level": "executivo",
        "start_date": (datetime.now() - timedelta(days=30)).isoformat(),
        "status": "active",
        "consultant_id": "admin",
        "created_at": (datetime.now() - timedelta(days=30)).isoformat(),
        "current_phase": 2,
        "overall_progress": 35,
        "phases": {
            "1": {
                "name": "Acolhimento & Diagnóstico",
                "description": "Acolhimento emocional, diagnóstico 360° e plano de ação individual",
                "status": "completed",
                "progress": 100,
                "start_date": (datetime.now() - timedelta(days=30)).isoformat(),
                "end_date": (datetime.now() - timedelta(days=18)).isoformat(),
                "activities": {
                    "acolhimento_emocional": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=28)).isoformat(),
                        "notes": "Processo inicial de adaptação, executiva mostrou determinação"
                    },
                    "diagnostico_360": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=24)).isoformat(),
                        "notes": "Forte experiência em gestão financeira e relacionamento com clientes"
                    },
                    "plano_acao_individual": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=18)).isoformat(),
                        "notes": "Foco em posições de Diretoria Comercial em fintechs e bancos digitais"
                    }
                }
            },
            "2": {
                "name": "Narrativa & Marca Pessoal",
                "description": "Construção de narrativa, marca pessoal e pitch de apresentação",
                "status": "in_progress",
                "progress": 33,
                "start_date": (datetime.now() - timedelta(days=18)).isoformat(),
                "end_date": None,
                "activities": {
                    "narrativa_marca_pessoal": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=12)).isoformat(),
                        "notes": "LinkedIn reformulado com foco em transformação digital bancária"
                    },
                    "pitch_apresentacao": {
                        "completed": False,
                        "date": None,
                        "notes": "Em desenvolvimento, próxima sessão na quinta-feira"
                    },
                    "oratoria_visibilidade": {
                        "completed": False,
                        "date": None,
                        "notes": "Aguardando finalização do pitch"
                    }
                }
            },
            "3": {
                "name": "Preparação para o Mercado",
                "description": "ReSkilling, UpSkilling e preparação para entrevistas",
                "status": "pending",
                "progress": 0,
                "start_date": None,
                "end_date": None,
                "activities": {
                    "reskilling_upskilling": {"completed": False, "date": None, "notes": ""},
                    "simulacoes_entrevistas": {"completed": False, "date": None, "notes": ""},
                    "relatorio_prontidao": {"completed": False, "date": None, "notes": ""}
                }
            },
            "4": {
                "name": "Conexão com o Mercado",
                "description": "Mentorias, busca ativa e rede de conexões",
                "status": "pending",
                "progress": 0,
                "start_date": None,
                "end_date": None,
                "activities": {
                    "mentorias_profissionais": {"completed": False, "date": None, "notes": ""},
                    "busca_ativa_posicoes": {"completed": False, "date": None, "notes": ""},
                    "rede_conexoes": {"completed": False, "date": None, "notes": ""},
                    "arenas_visibilidade": {"completed": False, "date": None, "notes": ""}
                }
            },
            "5": {
                "name": "Acompanhamento & Consolidação",
                "description": "Relatórios de progresso e dossiê final de transição",
                "status": "pending",
                "progress": 0,
                "start_date": None,
                "end_date": None,
                "activities": {
                    "relatorios_digitais": {"completed": False, "date": None, "notes": ""},
                    "indicadores_progresso": {"completed": False, "date": None, "notes": ""},
                    "dossie_final": {"completed": False, "date": None, "notes": ""}
                }
            }
        }
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Roberto Oliveira",
        "email": "roberto.oliveira@email.com",
        "phone": "(11) 97777-9999",
        "company": "Indústria Química XPTO",
        "position": "Diretor de Operações",
        "level": "executivo",
        "start_date": (datetime.now() - timedelta(days=90)).isoformat(),
        "status": "active",
        "consultant_id": "admin",
        "created_at": (datetime.now() - timedelta(days=90)).isoformat(),
        "current_phase": 5,
        "overall_progress": 95,
        "phases": {
            "1": {
                "name": "Acolhimento & Diagnóstico",
                "description": "Acolhimento emocional, diagnóstico 360° e plano de ação individual",
                "status": "completed",
                "progress": 100,
                "start_date": (datetime.now() - timedelta(days=90)).isoformat(),
                "end_date": (datetime.now() - timedelta(days=78)).isoformat(),
                "activities": {
                    "acolhimento_emocional": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=88)).isoformat(),
                        "notes": "Excelente engajamento desde o início do processo"
                    },
                    "diagnostico_360": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=85)).isoformat(),
                        "notes": "Perfil sólido em gestão industrial, foco em sustentabilidade"
                    },
                    "plano_acao_individual": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=78)).isoformat(),
                        "notes": "Estratégia para posições de CEO em indústrias sustentáveis"
                    }
                }
            },
            "2": {
                "name": "Narrativa & Marca Pessoal",
                "description": "Construção de narrativa, marca pessoal e pitch de apresentação",
                "status": "completed",
                "progress": 100,
                "start_date": (datetime.now() - timedelta(days=78)).isoformat(),
                "end_date": (datetime.now() - timedelta(days=62)).isoformat(),
                "activities": {
                    "narrativa_marca_pessoal": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=72)).isoformat(),
                        "notes": "Marca pessoal forte em sustentabilidade industrial"
                    },
                    "pitch_apresentacao": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=68)).isoformat(),
                        "notes": "Pitch impactante com cases de sucesso em ESG"
                    },
                    "oratoria_visibilidade": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=62)).isoformat(),
                        "notes": "Palestrante em conferência sobre indústria 4.0"
                    }
                }
            },
            "3": {
                "name": "Preparação para o Mercado",
                "description": "ReSkilling, UpSkilling e preparação para entrevistas",
                "status": "completed",
                "progress": 100,
                "start_date": (datetime.now() - timedelta(days=62)).isoformat(),
                "end_date": (datetime.now() - timedelta(days=45)).isoformat(),
                "activities": {
                    "reskilling_upskilling": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=58)).isoformat(),
                        "notes": "MBA em ESG e Sustentabilidade - FGV concluído"
                    },
                    "simulacoes_entrevistas": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=50)).isoformat(),
                        "notes": "Excelente performance em todas as simulações"
                    },
                    "relatorio_prontidao": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=45)).isoformat(),
                        "notes": "Altamente qualificado para posições de liderança"
                    }
                }
            },
            "4": {
                "name": "Conexão com o Mercado",
                "description": "Mentorias, busca ativa e rede de conexões",
                "status": "completed",
                "progress": 100,
                "start_date": (datetime.now() - timedelta(days=45)).isoformat(),
                "end_date": (datetime.now() - timedelta(days=15)).isoformat(),
                "activities": {
                    "mentorias_profissionais": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=40)).isoformat(),
                        "notes": "3 mentorias com CEOs da indústria química"
                    },
                    "busca_ativa_posicoes": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=30)).isoformat(),
                        "notes": "5 oportunidades identificadas, 3 em processo avançado"
                    },
                    "rede_conexoes": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=25)).isoformat(),
                        "notes": "Conexões estratégicas com headhunters especializados"
                    },
                    "arenas_visibilidade": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=15)).isoformat(),
                        "notes": "Participação em 2 eventos de networking setorial"
                    }
                }
            },
            "5": {
                "name": "Acompanhamento & Consolidação",
                "description": "Relatórios de progresso e dossiê final de transição",
                "status": "in_progress",
                "progress": 67,
                "start_date": (datetime.now() - timedelta(days=15)).isoformat(),
                "end_date": None,
                "activities": {
                    "relatorios_digitais": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=12)).isoformat(),
                        "notes": "Dashboard de acompanhamento implementado"
                    },
                    "indicadores_progresso": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=8)).isoformat(),
                        "notes": "Métricas excelentes em todos os indicadores"
                    },
                    "dossie_final": {
                        "completed": False,
                        "date": None,
                        "notes": "Aguardando confirmação de contratação para finalização"
                    }
                }
            }
        }
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Mariana Costa",
        "email": "mariana.costa@email.com",
        "phone": "(11) 96666-1111",
        "company": "Startup FinTech",
        "position": "CPO - Chief Product Officer",
        "level": "executivo",
        "start_date": (datetime.now() - timedelta(days=15)).isoformat(),
        "status": "active",
        "consultant_id": "admin",
        "created_at": (datetime.now() - timedelta(days=15)).isoformat(),
        "current_phase": 1,
        "overall_progress": 20,
        "phases": {
            "1": {
                "name": "Acolhimento & Diagnóstico",
                "description": "Acolhimento emocional, diagnóstico 360° e plano de ação individual",
                "status": "in_progress",
                "progress": 67,
                "start_date": (datetime.now() - timedelta(days=15)).isoformat(),
                "end_date": None,
                "activities": {
                    "acolhimento_emocional": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=12)).isoformat(),
                        "notes": "Primeira sessão muito positiva, boa receptividade"
                    },
                    "diagnostico_360": {
                        "completed": True,
                        "date": (datetime.now() - timedelta(days=8)).isoformat(),
                        "notes": "Perfil forte em produtos digitais e UX, experiência em startups"
                    },
                    "plano_acao_individual": {
                        "completed": False,
                        "date": None,
                        "notes": "Agendado para esta semana, foco em scale-ups e grandes techs"
                    }
                }
            },
            "2": {
                "name": "Narrativa & Marca Pessoal",
                "description": "Construção de narrativa, marca pessoal e pitch de apresentação",
                "status": "pending",
                "progress": 0,
                "start_date": None,
                "end_date": None,
                "activities": {
                    "narrativa_marca_pessoal": {"completed": False, "date": None, "notes": ""},
                    "pitch_apresentacao": {"completed": False, "date": None, "notes": ""},
                    "oratoria_visibilidade": {"completed": False, "date": None, "notes": ""}
                }
            },
            "3": {
                "name": "Preparação para o Mercado",
                "description": "ReSkilling, UpSkilling e preparação para entrevistas",
                "status": "pending",
                "progress": 0,
                "start_date": None,
                "end_date": None,
                "activities": {
                    "reskilling_upskilling": {"completed": False, "date": None, "notes": ""},
                    "simulacoes_entrevistas": {"completed": False, "date": None, "notes": ""},
                    "relatorio_prontidao": {"completed": False, "date": None, "notes": ""}
                }
            },
            "4": {
                "name": "Conexão com o Mercado",
                "description": "Mentorias, busca ativa e rede de conexões",
                "status": "pending",
                "progress": 0,
                "start_date": None,
                "end_date": None,
                "activities": {
                    "mentorias_profissionais": {"completed": False, "date": None, "notes": ""},
                    "busca_ativa_posicoes": {"completed": False, "date": None, "notes": ""},
                    "rede_conexoes": {"completed": False, "date": None, "notes": ""},
                    "arenas_visibilidade": {"completed": False, "date": None, "notes": ""}
                }
            },
            "5": {
                "name": "Acompanhamento & Consolidação",
                "description": "Relatórios de progresso e dossiê final de transição",
                "status": "pending",
                "progress": 0,
                "start_date": None,
                "end_date": None,
                "activities": {
                    "relatorios_digitais": {"completed": False, "date": None, "notes": ""},
                    "indicadores_progresso": {"completed": False, "date": None, "notes": ""},
                    "dossie_final": {"completed": False, "date": None, "notes": ""}
                }
            }
        }
    }
]

# Salvar os dados
with open('data/executives.json', 'w', encoding='utf-8') as f:
    json.dump(demo_executives, f, indent=2, ensure_ascii=False)

print("✅ Dados simulados criados com sucesso!")
print(f"📊 {len(demo_executives)} executivos adicionados com diferentes progressos nas 5 fases")
print("🎯 Agora você pode visualizar o cumprimento da metodologia no dashboard!")
