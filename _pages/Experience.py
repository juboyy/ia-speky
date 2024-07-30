import reveal_slides as rs

sample_markdown = r"""
# EXPERIÊNCIA NA INDÚSTRIA
Breve visão geral da minha experiência até o momento.
---


## Dell Technologies
`Estagiário de Inverno em Engenharia de Software`
</br>
``Jan-Maio 2024``
<div style='text-align: justify'><b>
<li>
Desenvolvi e implementei recursos para uma ferramenta de orquestração de API baseada em estados, garantindo integração perfeita e coordenação de vários serviços dentro de uma arquitetura baseada em microsserviços.</li><br>
<li>Projetei chatbots e ferramentas para fornecer insights e informações sobre pedidos usando Prompt Engineering.</li><br> 
<li>Conduzi pesquisas e desenvolvi um relatório abrangente sobre o tratamento de cenários NULL no MongoDB, implementando soluções para operações de leitura e gravação eficientes e sem erros.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
Microsserviços, Large Language Model (LLM), Small Language Model (SLM), Fine Tuning, Vector Database, Prompt Engineering, Docker, Kubernetes, RabbitMQ, orquestração, Golang, Python, MongoDB, API
</div>
---
## NoShitSecurity
`Estagiário de Arquitetura e Engenharia em Nuvem`
</br>
`Dez-Ago 2023`
<div style='text-align: justify'><b>
<li>Desenvolve e implanta infraestrutura resiliente em nuvem Azure.</li><br>
<li>Avalia a postura de segurança, identifica pontos fortes e fracos, aplica pensamento avançado e recomenda correções</li><br> 
<li>Utiliza as últimas tendências e técnicas líderes do setor para hospedar um evento mundial de captura da bandeira.</li><br> 
<li>Desenvolve ou implementa ferramentas de código aberto ou de terceiros para reduzir a exposição ou proteger a infraestrutura em nuvem</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
Arquitetura em Nuvem Azure, Engenharia de Segurança Azure, Monitor Azure, máquina virtual, redes virtuais, Cosmos DB, Recuperação de Desastres, Firewall e Defender Azure, Funções Azure, Blueprints Azure, Gerenciamento de Diretório Ativo de Sistemas em Nuvem e Pontos Finais, Criptografia e ferramentas de criptografia, Ferramentas de varredura de rede e sistema, Inteligência de código aberto (OSINT)

</div>
---
## Dell Technology
`Estagiário de Verão em Engenharia de Software`
</br>
`Maio-Julho 2023`
<div style='text-align: justify'><b>
<li>Colaborou com a equipe para implementar várias ferramentas de automação, garantindo o fluxo adequado e a gestão eficiente de pedidos.</li><br>
<li>Predição de cancelamento de pedidos usando algoritmos de aprendizado de máquina. </li><br> 
<li>Examinar os fatores que contribuem para o cancelamento de pedidos, identificando e abordando lacunas no sistema.</li><br> 
<li>Analisou dados para identificar fatores que contribuem para o cancelamento de pedidos e retenções do sistema, abordando lacunas no sistema para reduzir o cancelamento de pedidos e melhorar a eficiência geral.</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
Mineração de Dados, Análise de Dados, JSON, Python/R, Visualização de Dados, Framework Orange, Jupyter Notebook, Excel, Algoritmos de Aprendizado de Máquina, Automação, Pipeline ETL.

</div>
---
## NoShitSecurity
`Estagiário`
</br>
`Jun 2022 - Abril 2023`
<div style='text-align: justify'><b>
<li>Projeta e conduz pesquisas para garantir a segurança da infraestrutura em nuvem.</li><br>
<li>Utiliza técnicas avançadas de endurecimento de configuração para melhorar a segurança de VMs e cargas de trabalho.</li><br> 
<li>Assegura a integridade do sistema com políticas padrão do setor e controles de segurança em camadas.</li><br> 
<li>Alavanca as ferramentas do Azure Defender para produzir e manter uma postura de segurança mais saudável</li><br>
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
Linux, Lynis, Metasploit, NIST, Política, PowerShell, Python, Red Team, Relatórios, Sentinel, SIEM, Splunk, Estratégia, Redação Técnica, VPN Unix, Avaliação de Vulnerabilidades, Servidor Windows

</div>
---
## Virtually Testing Foundation 
`Estagiário de Segurança Cibernética`
</br>
`Maio-Julho 2022`
<div style='text-align: justify'><b>
<li>Mantém conhecimento técnico participando de várias oficinas e cursos online </li><br>
<li>Gerencia e produz documentação técnica, guias de processo e conteúdo relacionado à segurança cibernética</li><br> 
<li>Concluiu com sucesso todos os desafios de captura da bandeira atribuídos</li><br> 
</b>
</div>
Tecnologias Utilizadas
--
<b>Tecnologias Utilizadas</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style='text-align: justify'>
Segurança e Engenharia em Nuvem Básica, Splunk, Inteligência de Código Aberto (OSINT), Microsoft Azure Active Directory, MITRE ATT&CK 
</div>
"""
st.title("Experience")
currState = rs.slides(
    sample_markdown,
    theme="dracula",
    height=600,
    config={
        "transition": "slide",
        "width": 1100,
        "height": 1100,
        "center": True,
        "margin": 0.10,
        "scale_range": [0.1, 3.0],
    },
    initial_state={
        "indexf": -1,
    },
    markdown_props={"data-separator-vertical": "^--$"},
    key="foo",
)
