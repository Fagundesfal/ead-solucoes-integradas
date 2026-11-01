# Gera as páginas de serviço do site (SEO). Rodar: python3 tools/gerar_paginas.py
import json, os, html

BASE = "https://eadsolucoesintegradas.com.br"
WA = "https://wa.me/5511927415146?text="
CIDADES = ["Jandira", "Barueri", "Carapicuíba", "Osasco", "Itapevi", "Cotia", "Santana de Parnaíba", "São Paulo (capital)"]

PAGINAS = [
  {
    "slug": "portaria-de-obra",
    "titulo": "Portaria de Obra Terceirizada em Jandira, Barueri, Osasco e São Paulo",
    "h1": "Portaria de obra terceirizada",
    "desc": "Porteiro para obra em escala 12x36, dia e noite, com equipe própria, uniformizada e supervisionada. Controle de acesso, recebimento de materiais e bônus de 4 câmeras, DVR e alarme. Jandira, Barueri, Osasco e São Paulo.",
    "kw": "portaria de obra, porteiro para obra, portaria para canteiro de obras, controlador de acesso obra, portaria terceirizada, porteiro 12x36",
    "lead": "Porteiro para obra em escala 12x36, dia e noite, com equipe própria, uniformizada e supervisionada. A portaria é a porta de entrada do canteiro: quem entra, o que chega e o que sai passam por ela.",
    "msg": "Olá, gostaria de um orçamento de portaria de obra.",
    "blocos": [
      ("O que o porteiro da EAD faz na sua obra", [
        "Controla o acesso de funcionários, prestadores, visitantes e veículos, com registro de entrada e saída.",
        "Recebe entregas, materiais e encomendas, que ficam com a portaria até a equipe da obra chegar.",
        "Registra as ocorrências do posto e comunica a gestão da obra.",
        "Cobre o canteiro em escala 12x36: diurno das 7h às 19h e noturno das 19h às 7h.",
      ]),
      ("Bônus: 4 câmeras, DVR e alarme", [
        "No contrato de portaria, a EAD instala no início da obra 4 câmeras nos pontos de acesso, um DVR com as imagens gravadas e alarme para o canteiro, sem custo à parte.",
      ]),
      ("Por que terceirizar a portaria da obra com a EAD", [
        "Equipe própria registrada em CLT, com uniforme e EPIs.",
        "Check-in diário de cada porteiro no grupo do posto e folha de ponto assinada todo dia.",
        "Cobertura de faltas com equipe reserva, sem o posto ficar descoberto.",
        "Todo mês a construtora recebe holerites, FGTS por obra (CNO), INSS e folhas de ponto da equipe.",
      ]),
    ],
    "faq": [
      ("Qual a escala do porteiro de obra?", "Trabalhamos em 12x36: um posto diurno (7h às 19h) e um noturno (19h às 7h), cobrindo a obra 24 horas."),
      ("A portaria de obra inclui câmeras?", "Sim. No contrato de portaria a EAD instala 4 câmeras, DVR e alarme no início da obra, sem custo à parte."),
      ("Quais cidades vocês atendem?", "Jandira, Barueri, Carapicuíba, Osasco, Itapevi, Cotia, Santana de Parnaíba, a capital e outras cidades da Grande São Paulo e do interior, sob consulta."),
    ],
  },
  {
    "slug": "limpeza-pos-obra",
    "titulo": "Limpeza Pós-Obra para Construtoras – Grossa, Fina e Repasse | EAD",
    "h1": "Limpeza pós-obra para construtoras",
    "desc": "Limpeza pós-obra grossa, fina e repasse de entrega para construtoras e incorporadoras, com equipe CLT, encarregada na obra e controle de produção por unidade. Grande São Paulo e interior.",
    "kw": "limpeza pós-obra, limpeza pos obra, limpeza de obra, limpeza fina de obra, limpeza grossa de obra, limpeza para entrega de chaves",
    "lead": "Limpeza grossa, limpeza fina e repasse de entrega para deixar as unidades prontas para a entrega das chaves, com equipe própria e controle de produção por apartamento.",
    "msg": "Olá, gostaria de um orçamento de limpeza pós-obra.",
    "blocos": [
      ("Etapas da limpeza pós-obra", [
        "Limpeza grossa: retirada das proteções de obra, raspagem e remoção da sujeira e dos resíduos da própria limpeza.",
        "Limpeza fina: pisos, revestimentos, vidros e esquadrias, louças, metais, bancadas, portas, interruptores e tomadas, com produtos e utensílios que não riscam.",
        "Repasse de entrega: revisão final e remoção da poeira acumulada, com a equipe à disposição no período das vistorias.",
        "Unidade-protótipo executada primeiro, para aprovação da gestão da obra.",
      ]),
      ("Como organizamos a equipe", [
        "Auxiliares de limpeza e encarregada em tempo integral na obra, dimensionados pelo ritmo de liberação das torres e pavimentos.",
        "Controle de produção por apartamento e por pavimento, com medição por etapa concluída e aceita.",
        "Equipe CLT com uniforme, EPIs e documentação de SST por obra.",
        "Documentação mensal da equipe para a liberação das medições.",
      ]),
    ],
    "faq": [
      ("A limpeza pós-obra é cobrada por apartamento ou por m²?", "Montamos o preço pelo que fica mais claro para a obra: por apartamento, por pavimento ou por m², com as etapas grossa, fina e repasse separadas."),
      ("Vocês retiram entulho de construção?", "Levamos até a caçamba os resíduos gerados pela própria limpeza. Entulho de construção deixado por outras equipes e a caçamba são orçados à parte ou ficam com a obra."),
      ("Atendem obras fora da Grande São Paulo?", "Sim, sob consulta. Hoje mantemos equipe de limpeza pós-obra também no interior (Limeira)."),
    ],
  },
  {
    "slug": "limpeza-e-conservacao",
    "titulo": "Limpeza e Conservação Terceirizada para Empresas e Condomínios | EAD",
    "h1": "Limpeza e conservação terceirizada",
    "desc": "Auxiliar de limpeza terceirizada para escritórios, empresas, stands de vendas e condomínios, com equipe CLT, uniforme e cobertura de faltas. Jandira, Barueri, Osasco e São Paulo.",
    "kw": "limpeza e conservação, limpeza terceirizada, auxiliar de limpeza terceirizada, limpeza de escritório, limpeza de condomínio, empresa de limpeza Jandira",
    "lead": "Ambientes limpos e bem cuidados no dia a dia, sem atrapalhar a rotina: auxiliares de limpeza em posto fixo para escritórios, empresas, stands de vendas e condomínios.",
    "msg": "Olá, gostaria de um orçamento de limpeza e conservação.",
    "blocos": [
      ("O que inclui", [
        "Limpeza diária de pisos, mesas, superfícies e mobiliário.",
        "Banheiros, copa e áreas comuns.",
        "Recolhimento de lixo, vidros e portas internas ao alcance.",
        "Jornada integral ou meio período, conforme a necessidade do local.",
      ]),
      ("Como trabalhamos", [
        "Profissional selecionada, treinada e uniformizada.",
        "Supervisão pela gestão da EAD e cobertura de faltas, férias e afastamentos sem interromper o serviço.",
        "Equipe CLT com todos os encargos e benefícios incluídos no valor mensal.",
      ]),
    ],
    "faq": [
      ("Os produtos de limpeza estão inclusos?", "Depende do contrato: podemos incluir produtos e utensílios no valor mensal ou trabalhar com os materiais fornecidos pelo cliente."),
      ("Atendem meio período?", "Sim. Fazemos posto de meio período ou integral, de segunda a sexta ou na escala que o local precisar."),
    ],
  },
  {
    "slug": "recepcao-terceirizada",
    "titulo": "Recepção Terceirizada para Stands de Vendas e Escritórios | EAD",
    "h1": "Recepção terceirizada",
    "desc": "Recepcionista terceirizada para stands de vendas, plantões imobiliários e escritórios, com equipe uniformizada e cobertura de faltas. Jandira, Barueri, Osasco e São Paulo.",
    "kw": "recepção terceirizada, recepcionista terceirizada, recepcionista para stand de vendas, recepção para escritório, terceirização de recepção",
    "lead": "O primeiro contato do cliente com o seu empreendimento: recepcionistas preparadas para receber compradores e visitantes em stands de vendas e escritórios.",
    "msg": "Olá, gostaria de um orçamento de recepção.",
    "blocos": [
      ("O que a recepção da EAD faz", [
        "Recebe e direciona compradores, visitantes e fornecedores.",
        "Mantém o stand ou a recepção em ordem durante todo o expediente.",
        "Atende com uniforme, boa apresentação e linguagem adequada ao seu público.",
      ]),
      ("No mesmo contrato", [
        "Recepção, portaria e limpeza com um único fornecedor e contato direto com a gestão da EAD.",
        "Cobertura de faltas com equipe reserva.",
      ]),
    ],
    "faq": [
      ("Vocês atendem stand de vendas no fim de semana?", "Sim. Montamos a escala conforme o horário de funcionamento do stand, inclusive sábados, domingos e feriados."),
    ],
  },
]

ICONE_WA = open(os.path.join(os.path.dirname(__file__), "wa.svg"), encoding="utf-8").read()

def pagina(p):
    url = f"{BASE}/{p['slug']}/"
    blocos = "".join(
        f"<h2>{html.escape(t)}</h2>" + ("<ul class=\"checks\" style=\"list-style:none\">" + "".join(
            f"<li class=\"check\" style=\"font-weight:500\">{html.escape(i)}</li>" for i in itens) + "</ul>" if len(itens) > 1 else f"<p>{html.escape(itens[0])}</p>")
        for t, itens in p["blocos"])
    faq = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in p["faq"])
    outras = "".join(
        f"<a class=\"card\" href=\"/{o['slug']}/\"><h3>{html.escape(o['h1'])}</h3><p>{html.escape(o['lead'][:110])}…</p></a>"
        for o in PAGINAS if o["slug"] != p["slug"])
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Service", "name": p["h1"], "description": p["desc"], "url": url,
             "provider": {"@id": f"{BASE}/#empresa", "@type": "LocalBusiness", "name": "EAD Soluções Integradas",
                          "telephone": "+55-11-92741-5146",
                          "address": {"@type": "PostalAddress", "streetAddress": "Av. Carmine Gragnano, 48 – Sala 10 – Centro",
                                      "addressLocality": "Jandira", "addressRegion": "SP", "postalCode": "06600-010", "addressCountry": "BR"}},
             "areaServed": [c.replace(" (capital)", "") for c in CIDADES]},
            {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{BASE}/"},
                {"@type": "ListItem", "position": 2, "name": p["h1"], "item": url}]},
        ],
    }
    wa = WA + p["msg"].replace(" ", "%20").replace(",", "%2C")
    cidades = "".join(f"<span>{c}</span>" for c in CIDADES)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(p['titulo'])}</title>
<meta name="description" content="{html.escape(p['desc'])}">
<meta name="keywords" content="{html.escape(p['kw'])}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(p['titulo'])}">
<meta property="og:description" content="{html.escape(p['desc'])}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/og-ead.jpg">
<meta name="theme-color" content="#071634">
<link rel="icon" type="image/png" href="/logo-ead-web.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Public+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<nav>
  <div class="wrap nav-in">
    <a class="brand" href="/" aria-label="EAD Soluções Integradas – início"><img src="/logo-ead-web.png" alt="EAD" width="60" height="42" style="height:42px;width:auto"><b>SOLUÇÕES INTEGRADAS</b></a>
    <div class="links">
      <a href="/portaria-de-obra/">Portaria de obra</a>
      <a href="/limpeza-pos-obra/">Limpeza pós-obra</a>
      <a href="/limpeza-e-conservacao/">Limpeza</a>
      <a href="/recepcao-terceirizada/">Recepção</a>
      <a href="/#contato">Contato</a>
    </div>
    <a class="btn" href="{wa}" target="_blank" rel="noopener">Pedir orçamento</a>
  </div>
</nav>
<header class="hero on-dark">
  <div class="wrap">
    <p class="breadcrumb"><a href="/">Início</a> › {html.escape(p['h1'])}</p>
    <h1>{html.escape(p['h1'])}</h1>
    <p class="lead">{html.escape(p['lead'])}</p>
    <div class="ctas"><a class="btn" href="{wa}" target="_blank" rel="noopener">Pedir orçamento no WhatsApp</a><a class="btn ghost" href="/">Conhecer a EAD</a></div>
  </div>
</header>
<section>
  <div class="wrap prose">
    {blocos}
    <h2>Onde atendemos</h2>
    <p>Escritório em Jandira/SP. Atendemos a região oeste e a Grande São Paulo, a capital e o interior, sob consulta.</p>
    <div class="cities">{cidades}</div>
    <h2>Perguntas frequentes</h2>
    <div class="faq">{faq}</div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="head"><p class="eyebrow">Outros serviços</p><h2>No mesmo contrato</h2></div>
    <div class="more">{outras}</div>
  </div>
</section>
<section id="contato" class="contact on-dark">
  <div class="wrap two">
    <div>
      <p class="eyebrow">Contato</p>
      <h2 style="margin-top:12px">Peça um orçamento</h2>
      <p class="lead">Fale com a gente e receba uma proposta para o seu local.</p>
      <a class="btn" href="{wa}" target="_blank" rel="noopener">Pedir orçamento no WhatsApp</a>
    </div>
    <div class="clist">
      <div class="citem"><div><span>WhatsApp</span><a href="https://wa.me/5511927415146" target="_blank" rel="noopener">(11) 92741-5146</a></div></div>
      <div class="citem"><div><span>E-mail</span><a href="mailto:comercial@eadsolucoesintegradas.com.br">comercial@eadsolucoesintegradas.com.br</a></div></div>
      <div class="citem"><div><span>Instagram</span><a href="https://www.instagram.com/eadsi_/" target="_blank" rel="noopener">@eadsi_</a></div></div>
      <div class="citem"><div><span>Escritório</span>Av. Carmine Gragnano, 48 – Sala 10 – Centro – Jandira/SP – CEP 06600-010</div></div>
    </div>
  </div>
</section>
<footer>
  <div class="wrap foot">
    <span>© 2026 EAD Soluções Integradas Ltda · CNPJ 65.053.848/0001-24</span>
    <span><a href="/">Início</a> · <a href="/portaria-de-obra/">Portaria de obra</a> · <a href="/limpeza-pos-obra/">Limpeza pós-obra</a> · <a href="/limpeza-e-conservacao/">Limpeza e conservação</a> · <a href="/recepcao-terceirizada/">Recepção</a></span>
  </div>
</footer>
<a class="wa" href="https://wa.me/5511927415146" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">{ICONE_WA}</a>
</body>
</html>
"""

raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for p in PAGINAS:
    d = os.path.join(raiz, p["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(pagina(p))
urls = [f"{BASE}/"] + [f"{BASE}/{p['slug']}/" for p in PAGINAS]
open(os.path.join(raiz, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{u}</loc><lastmod>2026-11-01</lastmod></url>\n" for u in urls) + "</urlset>\n")
open(os.path.join(raiz, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print("ok", len(PAGINAS))
