import streamlit as st
import streamlit.components.v1 as components

# Define o conteúdo HTML da página da Ordem do Dia
html_content = """
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ordem do Dia - Projetos de Lei</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: white !important;
            color: black !important;
        }
        h1 {
            color: black !important;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-family: Arial, sans-serif;
            font-size: 12px;
        }

        th {
            background-color: #2c3e50;
            color: white;
            padding: 10px;
            text-align: left;
            border: 1px solid #ddd;
        }

        td {
            padding: 8px;
            border: 1px solid #ddd;
            vertical-align: top;
            color: #333;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        .favoravel {
            color: green !important;
            font-weight: bold;
        }

        .contrario {
            color: red !important;
            font-weight: bold;
        }

        .sem-competencia {
            color: #666 !important;
        }

        .ementa {
            font-weight: bold;
            font-size: 11px;
        }

        .briefing {
            font-size: 10px;
            font-style: italic;
        }
        .novo {
            background-color: #ffc107;
            color: #000;
            padding: 2px 5px;
            border-radius: 3px;
            font-size: 10px;
            font-weight: bold;
            margin-left: 5px;
        }
    </style>
</head>

<body>
    <h1>Ordem do Dia - Sessão Ordinária 14/10/2025 a 16/10/2025</h1>

    <table>
        <thead>
            <tr>
                <th style="width: 3%;">Nº</th>
                <th style="width: 5%;">Tipo</th>
                <th style="width: 7%;">Nº/Ano</th>
                <th style="width: 15%;">Autor</th>
                <th style="width: 20%;">Ementa</th>
                <th style="width: 20%;">Briefing</th>
                <th style="width: 20%;">Pareceres dos Órgãos</th>
                <th style="width: 10%;">Emendas/Substitutivos</th>
            </tr>
        </thead>
        <tbody>
            <!-- Projeto 1 -->
            <tr>
                <td>1</td>
                <td>PLC</td>
                <td>164/2024</td>
                <td>Carlo Caiado e outros.</td>
                <td class="ementa">Dispõe sobre a regulamentação da atividade econômica através transporte de
                    passageiros na Lagoa da Tijuca, Canal de Marapendi e Canal da Barra</td>
                <td class="briefing">Regulamenta transporte de passageiros e cargas nas lagoas da AP4</td>
                <td>
                    <span class="sem-competencia">SMTR: Sem competência (sugere CCPAR)</span><br>
                    <span class="favoravel">SMDUE: Favorável com sugestão de revisão dos arts. 3º e 7º para não
                        restringir a livre iniciativa e concorrência.</span><br>
                    SMCG, SMFP, CCPAR: Pendentes
                </td>
                <td><span title="Regulamenta o transporte de passageiros e cargas nas lagoas da AP4, definindo critérios para permissão, cadastramento e operação.">Substitutivo Nº 1</span></td>
            </tr>

            <!-- Projeto 2 -->
            <tr>
                <td>2</td>
                <td>PL</td>
                <td>2886/2024</td>
                <td>Dr. Rogério Amorim, Carlos Bolsonaro, Diego Faro</td>
                <td class="ementa">Inclui a Semana Municipal de Combate ao Aborto no Calendário Oficial</td>
                <td class="briefing">Semana de 1º a 8 de outubro sobre combate ao aborto</td>
                <td><span class="contrario">SMS: Contrário. A proposta pode gerar estigma e desinformação, além de interferir em políticas de saúde pública já estabelecidas.</span><span class="novo">NOVO!</span></td>
                <td><span title="Altera o texto do projeto para 'Combate ao Aborto Ilegal'.">Emenda Nº 1</span></td>
            </tr>

            <!-- Projeto 3 -->
            <tr>
                <td>3</td>
                <td>PL</td>
                <td>156/2025</td>
                <td>Marcelo Diniz et al.</td>
                <td class="ementa">Fiscalização digital da cobrança de vagas de estacionamento em vias públicas</td>
                <td class="briefing">Sistema digital para fiscalização e cobrança de estacionamento com reconhecimento
                    de placas e GPS</td>
                <td>
                    <span class="sem-competencia">SMTR: Sem competência</span><br>
                    <span class="sem-competencia">CET-RIO: Sem competência</span><br>
                    <span class="favoravel">SEOP: Nada a opor</span><br>
                    <span class="sem-competencia">IPLANRIO: Sem competência</span><br>
                    <span class="favoravel">CCPAR: Nada a opor</span>
                </td>
                <td><span title="Dispõe sobre a implementação e operação do Sistema de Área Azul Digital, estabelece normas para fiscalização, pagamento e utilização, e cria o Fundo Municipal da Área Azul Digital (FMAAD).">Substitutivo Nº 1 <span class="novo">NOVO!</span></span></td>
            </tr>

            <!-- Projeto 4 -->
            <tr>
                <td>4</td>
                <td>PL</td>
                <td>573/2025</td>
                <td>Tânia Bastos</td>
                <td class="ementa">Inclui Praça São Lucas e entorno (Vila Cruzeiro) como Polo Gastronômico e Cultural
                </td>
                <td class="briefing">Praça São Lucas e entorno como Polo na Lei Geral dos Polos</td>
                <td><span class="favoravel">SMC: Nada a opor</span><span class="novo">NOVO!</span></td>
                <td>-</td>
            </tr>

            <!-- Projeto 5 -->
            <tr>
                <td>5</td>
                <td>PL</td>
                <td>3260-A/2024</td>
                <td>Carlo Caiado</td>
                <td class="ementa">Instalação de câmeras de monitoramento em vias públicas por particulares</td>
                <td class="briefing">Normas para instalação de câmeras e cessão de imagens ao COR-Rio, CIVITAS e SESP
                </td>
                <td>
                    <span class="sem-competencia">SEOP: Sem competência</span><br>
                    <span class="favoravel">GP/COR: Favorável, com sugestão de acrescentar dispositivos de atendimento
                        à LGPD.</span><br>
                    <span class="favoravel">CVL/CIVITAS: Favorável</span>
                </td>
                <td><span title="Ajusta os artigos 1º e 3º para clarificar a cessão de imagens mediante convênios específicos.">Emenda Nº 1</span></td>
            </tr>

            <!-- Projeto 6 -->
            <tr>
                <td>6</td>
                <td>PL</td>
                <td>197/2025</td>
                <td>Wagner Tavares</td>
                <td class="ementa">Inclui São Bento como Polo Gastronômico, Turístico e Cultural</td>
                <td class="briefing">Estrada do Galeão (5275-5344), Rua Praia do Belo Jardim e Av. Dezessete como Polo
                </td>
                <td><span class="favoravel">SMC: Nada a opor</span></td>
                <td>-</td>
            </tr>

            <!-- Projeto 7 -->
            <tr>
                <td>7</td>
                <td>PL</td>
                <td>1613/2019</td>
                <td>Junior da Lucinha</td>
                <td class="ementa">Discriminação do destino de multas de trânsito nos documentos de notificação</td>
                <td class="briefing">Obriga discriminação de onde serão aplicados os recursos de multas de trânsito</td>
                <td>
                    <span class="contrario">SEOP: Contrário</span><span class="novo">NOVO!</span><br>
                    GM: Pendente<br>
                    <span class="contrario">SMF: Contrário. A destinação das multas já é prevista no Código de Trânsito
                        Brasileiro. A implementação exigiria adaptação do sistema emissor, gerando aumento de
                        despesas.</span><br>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 8 -->
            <tr>
                <td>8</td>
                <td>PLC</td>
                <td>25/2021</td>
                <td>Rafael Aloisio Freitas</td>
                <td class="ementa">Altera Lei Complementar nº 226/2020 sobre mesas e cadeiras em áreas públicas</td>
                <td class="briefing">Alterações na regulamentação de mesas e cadeiras em espaços públicos e afastamento
                    frontal</td>
                <td>
                    <span class="contrario">SMDU: Contrário. A proposta altera termos como "licenciamento" para
                        "autorização" e reduz o prazo de análise de 30 para 5 dias, o que pode favorecer o uso indevido
                        da área pública.</span><br>
                    <span class="favoravel">CLF: Favorável com sugestões de alteração nos arts. 9º, 22 e 23.</span><br>
                    <span class="favoravel">CET-RIO: Nada a opor</span><br>
                    <span class="sem-competencia">SMAC: Sem competência</span><br>
                    <span class="sem-competencia">SECONSERVA: Sem competência</span>
                </td>
                <td><span title="Altera a lei sobre mesas e cadeiras, ajustando regras para ocupação de passeios, afastamentos e vagas de estacionamento em polos gastronômicos.">Substitutivo Nº 1<br>Emendas 1 e 2</span></td>
            </tr>

            <!-- Projeto 9 -->
            <tr>
                <td>9</td>
                <td>PLC</td>
                <td>176/2024</td>
                <td>Marcio Ribeiro</td>
                <td class="ementa">Altera redação sobre número máximo de táxis (1 para cada 180 habitantes)</td>
                <td class="briefing">Proporcionalidade de 1 veículo táxi para cada 180 habitantes</td>
                <td>
                    <span class="favoravel">SMTR/SEOP: Nada a opor</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 10 -->
            <tr>
                <td>10</td>
                <td>PLC</td>
                <td>16/2025</td>
                <td>Talita Galhardo, Pedro Duarte</td>
                <td class="ementa">Proíbe contratação de shows/eventos infantojuvenis com apologia ao crime/drogas</td>
                <td class="briefing">Veda contratação pública de eventos com expressão de apologia ao crime ou drogas
                    para público infantojuvenil</td>
                <td>
                    <span class="favoravel">SMAS: Favorável, com recomendações de substituir o termo "menor" por
                        "criança e adolescente" e destinar multas ao Fundo Municipal para Atendimento dos Direitos da
                        Criança e do Adolescente (FMADCA).</span><br>
                    <span class="contrario">SMC: Contrária. A vedação genérica pode dar margem a interpretações
                        subjetivas e censura prévia, o que é vedado pelo ordenamento jurídico.</span><br>
                    <span class="favoravel">RIOCENTRO: Favorável</span><br>
                    JUV-RIO: Pendente
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 11 -->
            <tr>
                <td>11</td>
                <td>PLC</td>
                <td>23/2025</td>
                <td>Carlo Caiado et al.</td>
                <td class="ementa">Regulamenta intervenção do Poder Executivo em imóveis com risco estrutural</td>
                <td class="briefing">Define critérios de intervenção em imóveis particulares conforme art. 284 da LC
                    270/2024</td>
                <td>
                    SMI:<br>
                    <span class="favoravel">- GEO-RIO: Favorável com ressalva de alterar a redação do art. 7º de "adotará"
                        para "poderá adotar", a fim de garantir maior razoabilidade e flexibilidade orçamentária.</span><br>
                    <span class="contrario">- RIO-ÁGUAS: Contrário. A proposta invade competências do Poder Executivo,
                        alterando atribuições de órgãos e gerando aumento de despesas, em afronta à Lei Orgânica do
                        Município.</span><br>
                    <span class="favoravel">SMDU: Favorável</span><br>
                    CVL: Ciente
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 12 -->
            <tr>
                <td>12</td>
                <td>PLC</td>
                <td>27/2025</td>
                <td>Leniel Borel</td>
                <td class="ementa">Cria Ronda de Proteção à Infância (RPI) para policiamento ostensivo</td>
                <td class="briefing">RPI para policiamento ostensivo diante de condutas lesivas a crianças e
                    adolescentes</td>
                <td>
                    <span class="favoravel">GM-Rio: Favorável, com observação sobre uma obscuridade entre os artigos
                        1º e 4º e a ressalva de que a GM-Rio deve atuar apenas em funções de prevenção e educação, sem
                        assumir funções estranhas à sua natureza.</span><br>
                    <span class="favoravel">SMAS: Favorável</span><br>
                    <span class="favoravel">SME: Nada a opor</span><br>
                    <span class="favoravel">SEOP: Nada a opor</span><br>
                    <span class="favoravel">SEDHIR: Nada a opor</span>
                </td>
                <td>
                    <span title="Modifica a ementa e o Art. 1º, estabelecendo diretrizes para a atuação integrada de proteção a crianças e adolescentes (RPI).">Emenda Modificativa Nº 1 (CCJ) <span class="novo">NOVO!</span></span><br>
                    <span title="Modifica o Art. 2º, definindo as atribuições da RPI, como proteger a integridade física e psicológica e apoiar instituições.">Emenda Modificativa Nº 2 (CCJ) <span class="novo">NOVO!</span></span><br>
                    <span title="Modifica o Art. 3º, prevendo capacitação contínua para os servidores da RPI.">Emenda Modificativa Nº 3 (CCJ) <span class="novo">NOVO!</span></span><br>
                    <span title="Modifica o Art. 10, determinando providências imediatas em situações de risco.">Emenda Modificativa Nº 4 (CCJ) <span class="novo">NOVO!</span></span><br>
                    <span title="Suprime os incisos IV, V, e VII do Art. 4º.">Emenda Supressiva Nº 5 (CCJ) <span class="novo">NOVO!</span></span>
                </td>
            </tr>

            <!-- Projeto 13 -->
            <tr>
                <td>13</td>
                <td>PLC</td>
                <td>42/2025</td>
                <td>Rocal</td>
                <td class="ementa">Cria o bairro Magarça por subdivisão do bairro de Guaratiba (AP5)</td>
                <td class="briefing">Criação do bairro Magarça na XXVI Região Administrativa</td>
                <td><span class="contrario">SMDU: Contrário.</span><span class="novo">NOVO!</span><br><span class="sem-competencia">SMI: Sem competência.</span><span class="novo">NOVO!</span></td>
                <td>-</td>
            </tr>

            <!-- Projeto 14 -->
            <tr>
                <td>14</td>
                <td>PLC</td>
                <td>49/2025</td>
                <td>Pedro Duarte</td>
                <td class="ementa">Altera § 5º do art. 371 da LC 270/2024 sobre grupamentos de interesse social</td>
                <td class="briefing">Excepciona normas menos restritivas para grupamentos habitacionais de interesse
                    social</td>
                <td>
                    <span class="sem-competencia">SMI: Sem competência</span><br>
                    <span class="contrario">SMDU: Contrário. A matéria já está contemplada de forma mais abrangente no
                        art. 520 da mesma Lei Complementar e em estudos recentes da SMDU.</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 15 -->
            <tr>
                <td>15</td>
                <td>PL</td>
                <td>1128/2025</td>
                <td>Diego Faro et al.</td>
                <td class="ementa">Política Municipal de Conscientização e Combate à Adultização e Sexualização Infantil
                </td>
                <td class="briefing">Prevenir, identificar e combater adultização, sexualização infantil e pornografia
                    em plataformas digitais</td>
                <td>
                    SMAS: Pendente<br>
                    <span class="favoravel">SME: Favorável</span><br>
                    SMS: Pendente
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 16 -->
            <tr>
                <td>16</td>
                <td>PL</td>
                <td>2906/2024</td>
                <td>Felipe Michel</td>
                <td class="ementa">Obriga apps de entrega a fornecer opção de entrega na porta da unidade</td>
                <td class="briefing">Aplicativos devem disponibilizar escolha entre entrega na portaria ou na porta da
                    unidade</td>
                <td>
                    <span class="contrario">SMDUE: Desfavorável. O projeto padece de vício de inconstitucionalidade
                        por ferir o princípio da livre iniciativa e concorrência.</span><br>
                    PROCON, SEDECON: Pendentes
                </td>
                <td><span title="A emenda suprime um artigo e o substitutivo inverte a lógica do projeto, proibindo que entregadores sejam obrigados a subir até a porta da unidade, com exceções.">Emenda Supressiva Nº 1<br>Substitutivo Nº 1</span></td>
            </tr>

            <!-- Projeto 17 -->
            <tr>
                <td>17</td>
                <td>PL</td>
                <td>437/2025</td>
                <td>Maíra do MST, Monica Benicio</td>
                <td class="ementa">Programa Memória, Verdade e Justiça Carioca - identificação de locais de repressão da
                    ditadura</td>
                <td class="briefing">Identificação pública de lugares de repressão política durante ditadura (1964-1985)
                </td>
                <td>
                    SMC: Pendente<br>
                    <span class="contrario">IRPH: Contrário. A proposta contraria o Plano Diretor (LC 270/2024), que
                        exige estudos técnicos e anuência do Conselho de Patrimônio Cultural para alterar o status de
                        proteção de um bem.</span><br>
                    <span class="sem-competencia">SEDHIR: Sem competência</span>
                </td>
                <td><span title="Modifica o Art. 4º para incluir como objetos do programa os locais listados no relatório da Comissão Nacional da Verdade.">Emenda Modificativa Nº 1</span></td>
            </tr>

            <!-- Projeto 18 -->
            <tr>
                <td>18</td>
                <td>PL</td>
                <td>748/2018</td>
                <td>Jair da Mendes Gomes</td>
                <td class="ementa">Programa Adote um Campo para implantação, reforma e manutenção de campos de futebol
                </td>
                <td class="briefing">Parcerias entre Poder Público e sociedade para campos públicos de futebol amador
                </td>
                <td><span class="favoravel">FPJ: Favorável (2018)</span><span class="novo">NOVO!</span><br><span class="sem-competencia">CVL/SUBEL: Sem competência (2018)</span><span class="novo">NOVO!</span></td>
                <td>-</td>
            </tr>

            <!-- Projeto 19 -->
            <tr>
                <td>19</td>
                <td>PL</td>
                <td>2069/2023</td>
                <td>Cesar Maia</td>
                <td class="ementa">Obrigação acessória em unidades comerciais do Município</td>
                <td class="briefing">Garantir acesso a informações sobre exercício de atividades econômicas</td>
                <td>
                    <span class="sem-competencia">SMFP: Sem competência</span><br>
                    CLF: Pendente<br>
                    <span class="favoravel">SMDEIS: Favorável</span>
                </td>
                <td><span title="Suprime o Art. 4º do projeto.">Emenda Supressiva Nº 1</span></td>
            </tr>

            <!-- Projeto 20 -->
            <tr>
                <td>20</td>
                <td>PL</td>
                <td>2626/2023</td>
                <td>Vera Lins</td>
                <td class="ementa">Instalação de hidrômetros no interior dos imóveis pelas concessionárias</td>
                <td class="briefing">Hidrômetros devem ser instalados dentro dos imóveis, vedada instalação em calçadas
                </td>
                <td>
                    <span class="contrario">RIOAGUAS: Contrário. A instalação interna dos hidrômetros prejudica a
                        prestação adequada dos serviços e a cobrança de uma tarifa mais justa.</span><br>
                    <span class="contrario">SMDUE: Contrário. Padece de inconstitucionalidade formal, pois compete à
                        União instituir diretrizes para o saneamento básico.</span><br>
                    PROCON: Pendente
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 21 -->
            <tr>
                <td>21</td>
                <td>PL</td>
                <td>2783/2024</td>
                <td>Thais Ferreira</td>
                <td class="ementa">Diretrizes para caminhabilidade segura de infâncias, mulheres e pessoas cuidadoras
                </td>
                <td class="briefing">Mecanismos de prevenção e proteção contra violência no meio urbano</td>
                <td>
                    <span class="favoravel">SMAS: Favorável</span><br>
                    <span class="favoravel">SME: Favorável</span><br>
                    <span class="favoravel">SMS: Nada a opor. Sugere oitiva da SECONSERVA, RIO-LUZ, GM, RIO-URBE, SMAC,
                        SMDUE, SEOP, SMTR, CET-RIO.</span><br>
                    <span class="contrario">SMTR: Contrário. O PL não especifica modais de transporte, cria atribuições
                        para o Executivo de forma indevida e a exigência de fraldários em estações, não prevista em
                        contrato, geraria desequilíbrio econômico-financeiro.</span><br>
                    <span class="sem-competencia">SPM-RIO: Sem competência</span><br>
                    <span class="sem-competencia">SEOP: Sem competência</span><br>
                    <span class="favoravel">SECONSERVA: Nada a opor</span><br>
                    <span class="sem-competencia">SMDUE: Sem competência</span><br>
                    <span class="favoravel">RIO-URBE: Nada a opor</span><br>
                    <span class="favoravel">RIO-LUZ: Nada a opor</span><br>
                    <span class="sem-competencia">GM-RIO: Sem competência</span><br>
                    <span class="favoravel">CET-RIO: Nada a opor</span>
                </td>
                <td><span title="Ajustam a redação do projeto, substituindo 'infâncias' por 'crianças', e detalham as diretrizes para mobiliário urbano, calçamento e mitigação de violências.">Emendas Modificativas 1 a 7</span></td>
            </tr>

            <!-- Projeto 22 -->
            <tr>
                <td>22</td>
                <td>PL</td>
                <td>2931/2024</td>
                <td>Luciana Novaes</td>
                <td class="ementa">Direito ao acompanhamento para idosos e PcDs em consultas e exames</td>
                <td class="briefing">Presença de acompanhante para idosos e PcDs em estabelecimentos de saúde</td>
                <td>
                    SMPD: Pendente<br>
                    <span class="favoravel">SMS: Favorável</span><br>
                    <span class="favoravel">SEID: Nada a opor</span><br>
                    <span class="favoravel">SEMESQV: Favorável</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 23 -->
            <tr>
                <td>23</td>
                <td>PL</td>
                <td>3195/2024</td>
                <td>Zico</td>
                <td class="ementa">Inclui Praça João Petini (Campo Grande) como Polo Gastronômico e Cultural</td>
                <td class="briefing">Praça na Rua Mauro de Almeida - Figueira como Polo</td>
                <td><span class="favoravel">SMTE: Nada a opor</span></td>
                <td>-</td>
            </tr>

            <!-- Projeto 24 -->
            <tr>
                <td>24</td>
                <td>PL</td>
                <td>3210/2024</td>
                <td>William Siri</td>
                <td class="ementa">Selo Empresa Amiga do Trabalhador Migrante e Refugiado</td>
                <td class="briefing">Reconhecimento a empresas que incentivam contratação de migrantes e refugiados</td>
                <td>
                    <span class="favoravel">SMTE: Nada a opor</span><br>
                    SECID: Pendente<br>
                    <span class="favoravel">SMAS: Nada a opor</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 25 -->
            <tr>
                <td>25</td>
                <td>PL</td>
                <td>3403/2024</td>
                <td>Monica Benicio</td>
                <td class="ementa">Considera Parada do Orgulho LGBTI+ de interesse cultural, social e histórico</td>
                <td class="briefing">Reconhecimento da Parada LGBTI+ realizada anualmente no Rio</td>
                <td>
                    <span class="favoravel">SMC: Favorável</span><br>
                    <span class="favoravel">CVL/CDS: Favorável</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 26 -->
            <tr>
                <td>26</td>
                <td>PL</td>
                <td>48/2025</td>
                <td>Paulo Messina</td>
                <td class="ementa">Política Municipal de Uso de Canabidiol (PMUC) para fins medicinais</td>
                <td class="briefing">Dispõe sobre uso medicinal de canabidiol no município</td>
                <td>SMS: Pendente</td>
                <td><span title="Modifica o Art. 5º, estabelecendo que o Poder Executivo regulamentará a Lei.">Emenda Modificativa Nº 1 (CCJ) <span class="novo">NOVO!</span></span></td>
            </tr>

            <!-- Projeto 27 -->
            <tr>
                <td>27</td>
                <td>PL</td>
                <td>74/2025</td>
                <td>Átila Nunes</td>
                <td class="ementa">Altera Lei 7.008/2021 sobre Circuito Carioca de Economia Solidária</td>
                <td class="briefing">Alterações em dispositivos sobre implantação e gestão do Circuito</td>
                <td><span class="favoravel">SMDE: Nada a opor</span></td>
                <td>-</td>
            </tr>

            <!-- Projeto 28 -->
            <tr>
                <td>28</td>
                <td>PL</td>
                <td>103/2025</td>
                <td>Salvino Oliveira</td>
                <td class="ementa">Programa Recicla Rio - incentivos à coleta de lixo no Carnaval</td>
                <td class="briefing">Destinação de resíduos coletados no Carnaval a grupos cadastrados</td>
                <td>
                    <span class="contrario">COMLURB: Contrário. A parceria com múltiplos grupos pode fragmentar a
                        operação de limpeza. Além disso, o custo com equipamentos (EPIs) deveria ser da iniciativa
                        privada (organizadores do evento), e não do erário municipal.</span><br>
                    SMAC: Pendente<br>
                    <span class="favoravel">RIOTUR: Favorável</span><br>
                    <span class="favoravel">SMTE: Nada a opor</span>
                </td>
                <td><span title="Modifica o caput do Art. 2º, para que a coleta seja realizada pelo órgão competente em parceria com grupos cadastrados.">Emenda Modificativa Nº 1 (CCJ) <span class="novo">NOVO!</span></span></td>
            </tr>

            <!-- Projeto 29 -->
            <tr>
                <td>29</td>
                <td>PL</td>
                <td>119/2025</td>
                <td>Jorge Canella</td>
                <td class="ementa">Veda parceria/patrocínio de empresas inadimplentes em eventos públicos</td>
                <td class="briefing">Proíbe empresas devedoras de tributos municipais de patrocinar eventos públicos
                </td>
                <td>
                    <span class="favoravel">SMC: Nada a opor com sugestões de incluir exceções justificadas, garantir
                        ampla defesa antes de sanções e definir melhor o conceito de "eventos promovidos, direta ou
                        indiretamente".</span><br>
                    <span class="sem-competencia">SMEL: Sem competência</span><br>
                    <span class="sem-competencia">SMF: Sem competência</span><br>
                    <span class="favoravel">SMH: Nada a opor</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 30 -->
            <tr>
                <td>30</td>
                <td>PL</td>
                <td>133/2025</td>
                <td>Fernando Armelau</td>
                <td class="ementa">Portal do Legado Olímpico para gestão dos equipamentos olímpicos</td>
                <td class="briefing">Plataforma digital para divulgação de gestão, utilização e manutenção</td>
                <td>
                    SMEL: Pendente<br>
                    SMIT: Sugerida a oitiva do órgão gestor
                </td>
                <td><span title="Modifica o Art. 6º, estabelecendo sanções para o descumprimento da Lei.">Emenda Modificativa Nº 1 (CCJ) <span class="novo">NOVO!</span></span></td>
            </tr>

            <!-- Projeto 31 -->
            <tr>
                <td>31</td>
                <td>PL</td>
                <td>181/2025</td>
                <td>Talita Galhardo</td>
                <td class="ementa">Internação compulsória de usuários de drogas</td>
                <td class="briefing">Poder Público deve internar compulsoriamente usuários em situação deteriorante</td>
                <td>
                    <span class="contrario">SMS: Contrário. A proposta fere o disposto na Lei Federal nº 10.216/2001,
                        que redireciona o modelo assistencial em saúde mental.</span><br>
                    <span class="sem-competencia">SMAS: Sem competência</span><br>
                    <span class="sem-competencia">SEDHIR: Sem competência</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 32 -->
            <tr>
                <td>32</td>
                <td>PL</td>
                <td>191/2025</td>
                <td>Tânia Bastos</td>
                <td class="ementa">Programa de Orientação, Predição e Prevenção à Pré-eclâmpsia</td>
                <td class="briefing">Reduzir incidência de pré-eclâmpsia entre gestantes na rede municipal</td>
                <td>SMS: Pendente</td>
                <td>-</td>
            </tr>

            <!-- Projeto 33 -->
            <tr>
                <td>33</td>
                <td>PL</td>
                <td>208/2025</td>
                <td>Wagner Tavares</td>
                <td class="ementa">Inclui Aterro do Cocotá como Polo Gastronômico, Turístico e Cultural</td>
                <td class="briefing">Ruas Capitão Barbosa, Praia da Bandeira e Praia de Olaria como Polo</td>
                <td>SMC: Pendente</td>
                <td>-</td>
            </tr>

            <!-- Projeto 34 -->
            <tr>
                <td>34</td>
                <td>PL</td>
                <td>264/2025</td>
                <td>Felipe Pires</td>
                <td class="ementa">Permite entrada de bebidas e alimentos em eventos patrocinados pela Prefeitura</td>
                <td class="briefing">Eventos municipais não podem vedar entrada de bebidas/alimentos para consumo
                    próprio</td>
                <td>
                    <span class="favoravel">RIOTUR: Nada a opor</span><br>
                    <span class="favoravel">RIOCENTRO: Favorável</span><br>
                    <span class="favoravel">SEDECON: Favorável</span>
                </td>
                <td><span title="Suprime o Art. 3º do Projeto de Lei.">Emenda Supressiva Nº 1 (CCJ) <span class="novo">NOVO!</span></span></td>
            </tr>

            <!-- Projeto 35 -->
            <tr>
                <td>35</td>
                <td>PL</td>
                <td>281/2025</td>
                <td>Vitor Hugo</td>
                <td class="ementa">Política de acesso à informação sobre compensações ambientais de cortes de árvores
                </td>
                <td class="briefing">Publicidade e monitoramento das compensações por corte de árvores</td>
                <td>
                    <span class="sem-competencia">SMIT: Sem competência</span><br>
                    SMAC: Pendente
                </td>
                <td><span title="Modifica o Art. 8º, determinando que o Poder Executivo regulamentará a Lei.">Emenda Modificativa Nº 1 (CCJ) <span class="novo">NOVO!</span></span></td>
            </tr>

            <!-- Projeto 36 -->
            <tr>
                <td>36</td>
                <td>PL</td>
                <td>283/2025</td>
                <td>Felipe Boró</td>
                <td class="ementa">Inclui Praça dos Salmos (Bangu) como Polo Gastronômico e Cultural</td>
                <td class="briefing">Praça dos Salmos em Bangu como Polo</td>
                <td><span class="favoravel">SMC: Favorável</span></td>
                <td>-</td>
            </tr>

            <!-- Projeto 37 -->
            <tr>
                <td>37</td>
                <td>PL</td>
                <td>295/2025</td>
                <td>Fabio Silva</td>
                <td class="ementa">Cadastro Municipal de Crianças Atípicas</td>
                <td class="briefing">Cadastro para crianças com TEA e outras deficiências neurológicas</td>
                <td>
                    <span class="favoravel">SMS: Nada a opor</span><br>
                    <span class="contrario">SME: Contrário. A proposta pode gerar conflito de competência com o
                        Instituto Helena Antipoff (IHA), órgão já responsável por esses alunos, enfraquecendo sua
                        função.</span><br>
                    <span class="contrario">SMAS: Contrário. O Cadastro Único (CadÚnico) já possui campo para
                        identificar pessoas com deficiência. Um novo sistema geraria duplicidade e aumento de
                        despesas.</span>
                </td>
                <td><span title="Modifica o Art. 5º, estabelecendo que o Poder Executivo regulamentará a Lei.">Emenda Modificativa Nº 1 (CCJ) <span class="novo">NOVO!</span></span></td>
            </tr>

            <!-- Projeto 38 -->
            <tr>
                <td>38</td>
                <td>PL</td>
                <td>359/2025</td>
                <td>Rick Azevedo</td>
                <td class="ementa">Ensino extracurricular de Noções de Direito do Trabalho nas escolas municipais</td>
                <td class="briefing">Atividade extracurricular sobre direito do trabalho na rede municipal</td>
                <td><span class="contrario">SME: Desfavorável. A proposta não se alinha à política de educação
                        integral, não é adequada à faixa etária dos alunos (4 a 15 anos) e não está prevista no Currículo
                        Carioca nem na BNCC.</span></td>
                <td>
                    <span title="Suprime os Arts. 5º, 6º e 7º do projeto original.">Emenda Supressiva Nº 1 (CCJ) <span class="novo">NOVO!</span></span><br>
                    <span title="Suprime os Arts. 5º, 6º e 7º do projeto original.">Emenda Supressiva Nº 2 (CCJ) <span class="novo">NOVO!</span></span><br>
                    <span title="Suprime os Arts. 5º, 6º e 7º do projeto original.">Emenda Supressiva Nº 3 (CCJ) <span class="novo">NOVO!</span></span>
                </td>
            </tr>

            <!-- Projeto 39 -->
            <tr>
                <td>39</td>
                <td>PL</td>
                <td>370/2025</td>
                <td>Marcelo Diniz</td>
                <td class="ementa">Responsabilidade urbanística de shoppings sobre impacto de delivery</td>
                <td class="briefing">Shoppings respondem por impactos na vizinhança dos serviços de entrega por app</td>
                <td>
                    <span class="favoravel">CET-RIO: Favorável</span><br>
                    <span class="sem-competencia">SEOP: Sem competência</span><br>
                    <span class="sem-competencia">SMI: Sem competência</span><br>
                    <span class="sem-competencia">SMDU: Sem competência</span>
                </td>
                <td><span title="Exige que shoppings destinem espaço físico coberto e exclusivo para os entregadores.">Emenda Modificativa Nº 1 (CCJ) <span class="novo">NOVO!</span></span></td>
            </tr>

            <!-- Projeto 40 -->
            <tr>
                <td>40</td>
                <td>PL</td>
                <td>389/2025</td>
                <td>Gigi Castilho</td>
                <td class="ementa">Sala Lilás nos CRAS para atendimento a mulheres em situação de violência</td>
                <td class="briefing">Espaço de acolhimento para mulheres vítimas de violência doméstica nos CRAS</td>
                <td>
                    <span class="contrario">SMAS: Contrário. A proposta não se coaduna com os serviços disponibilizados
                        pelos CRAS nem pelos CREAS.</span><br>
                    <span class="favoravel">SPM-RIO: Nada a opor, com a ressalva de que a implementação requer previsão
                        de recursos físicos, humanos e orçamentários.</span><br>
                    <span class="sem-competencia">SMS: Sem competência</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 41 -->
            <tr>
                <td>41</td>
                <td>PL</td>
                <td>439/2025</td>
                <td>Rodrigo Vizeu</td>
                <td class="ementa">Programa de Benefício à Adoção Responsável de Cães e Gatos</td>
                <td class="briefing">Incentivos à adoção responsável de animais em vulnerabilidade</td>
                <td>
                    <span class="favoravel">SMPDA: Nada a opor</span><br>
                    <span class="sem-competencia">S/IVISA: Sem competência</span><br>
                    <span class="contrario">SMF: Contrário. O projeto usurpa competência do Executivo, não apresenta
                        estimativa de impacto financeiro para o desconto no IPTU e possui critérios de difícil
                        fiscalização, o que o torna inexequível.</span>
                </td>
                <td>
                    <span title="Define que o programa será executado por meio de ações de prevenção e controle de zoonoses.">Emenda Modificativa Nº 1 (CCJ) <span class="novo">NOVO!</span></span><br>
                    <span title="Suprime o Art. 4º do Projeto de Lei.">Emenda Supressiva Nº 2 (CCJ) <span class="novo">NOVO!</span></span>
                </td>
            </tr>

            <!-- Projeto 42 -->
            <tr>
                <td>42</td>
                <td>PL</td>
                <td>478/2025</td>
                <td>Marcos Dias</td>
                <td class="ementa">Programa Escola Amiga do Autista baseado em ABA</td>
                <td class="briefing">Inclusão de estudantes com TEA com base em Análise do Comportamento Aplicada</td>
                <td>
                    <span class="contrario">SME: Contrária. A abordagem terapêutica ABA é competência da saúde, não da
                        educação. A rede já elabora planos individualizados e a proposta pode duplicar ações já
                        existentes.</span><br>
                    SEI-RIO, SMPD: Pendentes
                </td>
                <td>
                    <span title="Suprime o inciso IV do Art. 2º.">Emenda Supressiva Nº 1 (CCJ) <span class="novo">NOVO!</span></span><br>
                    <span title="Suprime o Art. 5º da proposição.">Emenda Supressiva Nº 2 (CCJ) <span class="novo">NOVO!</span></span><br>
                    <span title="Detalha que a capacitação ocorrerá de forma modular e acessível.">Emenda Modificativa Nº 3 (CCJ) <span class="novo">NOVO!</span></span>
                </td>
            </tr>

            <!-- Projeto 43 -->
            <tr>
                <td>43</td>
                <td>PL</td>
                <td>556/2025</td>
                <td>Flavio Pato</td>
                <td class="ementa">Supressão/poda de árvores em risco em imóveis de pessoas do CadÚnico</td>
                <td class="briefing">Município pode realizar poda/supressão em imóveis de cadastrados no CadÚnico</td>
                <td>
                    <span class="contrario">COMLURB: Contrário. A inclusão de rotinas em imóveis particulares geraria
                        impacto orçamentário e contratual, além de exigir replanejamento e análise de legalidade.</span><br>
                    <span class="sem-competencia">S/SUBPDEC: Sem competência</span><br>
                    SMAC: Pendente
                </td>
                <td><span title="Autoriza o Poder Executivo a promover a poda/supressão em imóveis do CadÚnico, mediante laudo técnico.">Emenda Modificativa Nº 1 (CCJ) <span class="novo">NOVO!</span></span></td>
            </tr>

            <!-- Projeto 44 -->
            <tr>
                <td>44</td>
                <td>PL</td>
                <td>580/2025</td>
                <td>Dr. Gilberto</td>
                <td class="ementa">Exigência de certidão criminal e laudo toxicológico de servidores que atuam com
                    crianças</td>
                <td class="briefing">Servidores que trabalham com crianças devem apresentar certidão e laudo
                    periodicamente</td>
                <td>
                    <span class="contrario">F/SUBGGC: Contrário. Invade competência privativa do Chefe do Poder
                        Executivo ao dispor sobre o regime jurídico dos servidores. As medidas podem afrontar princípios
                        constitucionais.</span><br>
                    <span class="sem-competencia">SMAS: Sem competência</span><br>
                    <span class="sem-competencia">SME: Sem competência</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 45 -->
            <tr>
                <td>45</td>
                <td>PL</td>
                <td>592/2025</td>
                <td>Willian Coelho</td>
                <td class="ementa">Inclui Encontro Anual Sepevolks no Calendário Oficial</td>
                <td class="briefing">Evento anual no mês de junho</td>
                <td><span class="favoravel">SMC: Nada a opor</span></td>
                <td>-</td>
            </tr>

            <!-- Projeto 46 -->
            <tr>
                <td>46</td>
                <td>PL</td>
                <td>600/2025</td>
                <td>Carlos Bolsonaro</td>
                <td class="ementa">Nomeia escolas como Gilbert K. Chesterton, C.S. Lewis e J.R.R. Tolkien</td>
                <td class="briefing">Três escolas inominadas receberão nomes dos autores</td>
                <td>
                    <span class="favoravel">SMC: Nada a opor</span><br>
                    <span class="favoravel">SME: Nada a opor</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 47 -->
            <tr>
                <td>47</td>
                <td>PL</td>
                <td>608/2025</td>
                <td>Diego Faro</td>
                <td class="ementa">Dia Municipal da Adoção Espiritual no Calendário Oficial</td>
                <td class="briefing">8 de outubro como Dia da Adoção Espiritual</td>
                <td>
                    <span class="favoravel">SMC: Nada a opor</span><br>
                    <span class="favoravel">CVL/CDR: Nada a opor</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 48 -->
            <tr>
                <td>48</td>
                <td>PL</td>
                <td>641/2025</td>
                <td>Helena Vieira</td>
                <td class="ementa">Incentivo financeiro-educacional "Pezinho de Meia" (poupança) para estudantes</td>
                <td class="briefing">Poupança para alunos de baixa renda do 7º ao 9º ano do ensino fundamental</td>
                <td>
                    <span class="sem-competencia">SME: Sem competência</span><br>
                    <span class="favoravel">SMAS: Nada a opor</span><br>
                    <span class="sem-competencia">SMF: Sem competência</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 49 -->
            <tr>
                <td>49</td>
                <td>PL</td>
                <td>679/2025</td>
                <td>Talita Galhardo</td>
                <td class="ementa">Obriga academias a ter convênio com clínica/médico para exames</td>
                <td class="briefing">Academias devem ter convênio para realização de exames periódicos e de matrícula
                </td>
                <td>
                    SMS: Pendente<br>
                    <span class="contrario">S/IVISA: Contrário. Legislar sobre o exercício de profissões é competência
                        exclusiva da União.</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 50 -->
            <tr>
                <td>50</td>
                <td>PL</td>
                <td>794/2025</td>
                <td>Dr. Rogério Amorim</td>
                <td class="ementa">Remissão e anistia de créditos tributários de cartórios (ISS subitem 21.01)</td>
                <td class="briefing">Remissão de ISS de cartórios com fatos geradores até setembro/2013</td>
                <td>
                    <span class="contrario">SMF: Contrária. A proposta tenta repristinar um benefício fiscal já
                        rejeitado, sem respaldo legal ou financeiro, sem estimativas fiscais e quebrando a isonomia
                        tributária.</span><br>
                    CVL: Ciente
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 51 -->
            <tr>
                <td>51</td>
                <td>PL</td>
                <td>801/2025</td>
                <td>Leonel de Esquerda</td>
                <td class="ementa">Declara patrimônio cultural imaterial os trabalhadores ambulantes das praias/orla
                </td>
                <td class="briefing">Camelôs e ambulantes das praias como patrimônio cultural carioca</td>
                <td>
                    <span class="contrario">IRPH: Contrário. A proposta contraria o Plano Diretor (LC 270/2024), que
                        exige estudos técnicos e anuência do Conselho de Patrimônio para tal declaração.</span><br>
                    <span class="contrario">SMTE: Contrário. A proposta é incompatível com os parâmetros legais para
                        patrimônio imaterial; o foco da proteção deveria ser a atividade econômica, não o
                        trabalhador.</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 52 -->
            <tr>
                <td>52</td>
                <td>PL</td>
                <td>840/2025</td>
                <td>Rosa Fernandes</td>
                <td class="ementa">Campanha de Prevenção ao Bullying e Cyberbullying no Calendário Oficial</td>
                <td class="briefing">Semana de 7 de abril - Dia Nacional de Combate ao Bullying</td>
                <td>
                    <span class="favoravel">SMC: Nada a opor</span><br>
                    <span class="favoravel">SMCT: Favorável</span>
                </td>
                <td>-</td>
            </tr>

            <!-- Projeto 53 -->
            <tr>
                <td>53</td>
                <td>PL</td>
                <td>1032/2025</td>
                <td>Deangeles Percy</td>
                <td class="ementa">Inclui Instituto Libertas como utilidade pública</td>
                <td class="briefing">Instituto Internacional para Bispos, Pastores e Ministros Evangélicos</td>
                <td>
                    <span class="favoravel">CVL/CDR: Nada a opor</span><br>
                    <span class="contrario">SMAS: Contrário. A instituição não foi localizada em visita técnica,
                        impossibilitando a avaliação.</span>
                </td>
                <td>-</td>
            </tr>

        </tbody>
    </table>

</body>

</html>
"""

# Configurações da página
st.set_page_config(
    page_title="Ordem do Dia - Câmara Municipal",
    layout="wide"
)

# Renderiza o componente HTML
# O uso de scrolling=True permite que o iframe tenha sua própria barra de rolagem se o conteúdo for maior que a altura.
components.html(html_content, height=1200, scrolling=True)

