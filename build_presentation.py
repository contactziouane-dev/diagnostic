# -*- coding: utf-8 -*-
"""
Full generator for index.html - Standalone Academic Presentation.
Includes all 22 slides, responsive 16:9 scaling, keyboard navigation,
speaker notes (modal S), grid overview (modal O), bullet builds, and print CSS.
"""

import os
import json
from generate_svgs import (
    get_svg_pyramide,
    get_svg_avant_apres,
    get_svg_dp_vs_pa,
    get_svg_signaux,
    get_svg_db9,
    get_svg_chaine_liaison,
    get_svg_pile_profinet,
    get_svg_architecture_complete
)

target_file = r"C:\Users\Utilisateur\.gemini\antigravity\scratch\presentation-reseaux-industriels\index.html"

# Slide data definition
slides = [
    # Slide 1: Titre
    {
        "id": 1,
        "section": "INTRODUCTION GÉNÉRALE",
        "title": "LES RÉSEAUX INDUSTRIELS",
        "subtitle": "Architecture, technologies et protocoles de communication",
        "badge": "Automatisme & Informatique Industrielle",
        "content": '''
        <div class="split-layout">
          <div class="col text-col" style="flex: 1.2;">
            <div class="academic-badge">COURS ACADÉMIQUE · NIVEAU MASTER / INGÉNIEUR</div>
            <h1 class="main-title">LES RÉSEAUX INDUSTRIELS</h1>
            <h2 class="sub-title">Architecture, technologies et protocoles de communication</h2>
            <p class="baseline">De la communication entre capteurs et automates jusqu'aux réseaux Ethernet industriels</p>
            
            <div class="card intro-meta-box">
              <div class="meta-item"><span class="meta-label">Présentateur :</span> <span class="editable-name" contenteditable="true" spellcheck="false" title="Cliquez pour modifier votre nom">[NOM]</span></div>
              <div class="meta-item"><span class="meta-label">Discipline :</span> Génie Électrique &amp; Automatisation Industrielle</div>
              <div class="meta-item"><span class="meta-label">Date :</span> Novembre 2026</div>
              <div class="meta-item"><span class="meta-label">Support :</span> Présentation interactive hors-ligne pour vidéoprojection</div>
            </div>

            <div class="nav-hint-pill">
              Utilisez les touches <kbd>→</kbd> <kbd>Espace</kbd> pour avancer, <kbd>O</kbd> pour la vue globale, <kbd>S</kbd> pour les notes, <kbd>F</kbd> pour le plein écran.
            </div>
          </div>

          <div class="col media-col" style="flex: 1;">
            <div class="img-frame">
              <img src="assets/image1.jpeg" alt="Armoire d'automatisation avec pupitre tactile et robot" onerror="handleImgError(this)">
              <div class="caption">Armoire d'automatisation moderne : intégration d'automates programmables, pupitre IHM et cellule robotisée</div>
            </div>
          </div>
        </div>
        ''',
        "notes": "Bonjour à toutes et à tous. Bienvenue à cette présentation consacrée aux réseaux industriels. Nous allons parcourir ensemble l'architecture globale de communication, depuis la liaison électrique élémentaire entre un capteur et un automate jusqu'aux technologies Ethernet déterministes de dernière génération."
    },

    # Slide 2: Plan général
    {
        "id": 2,
        "section": "SOMMAIRE",
        "title": "Plan général de la présentation",
        "subtitle": "Un parcours pédagogique structuré en quatre grands axes",
        "badge": "Organisation",
        "content": '''
        <div class="plan-grid">
          <div class="plan-card build-item">
            <div class="plan-num">01</div>
            <div class="plan-title">Problématique &amp; Évolution</div>
            <p class="plan-desc">Du câblage traditionnel point-à-point à la communication sur bus partagé. Pourquoi avons-nous éliminé les forêts de câbles ?</p>
            <span class="plan-tag">Diapositives 3 à 5</span>
          </div>

          <div class="plan-card build-item">
            <div class="plan-num">02</div>
            <div class="plan-title">Modèles &amp; Classifications</div>
            <p class="plan-desc">Degré d'ouverture (propriétaire, homogène, hétérogène) et la Pyramide de l'automatisation en 3 niveaux fonctionnels.</p>
            <span class="plan-tag">Diapositives 6 à 8</span>
          </div>

          <div class="plan-card build-item">
            <div class="plan-num">03</div>
            <div class="plan-title">PROFIBUS DP &amp; PROFIBUS PA</div>
            <p class="plan-desc">Étude approfondie : RS-485 vs MBP, connectique DB9, terminaison active, standard 4-20 mA et passerelle coupleur DP/PA.</p>
            <span class="plan-tag">Diapositives 9 à 16</span>
          </div>

          <div class="plan-card build-item">
            <div class="plan-num">04</div>
            <div class="plan-title">L'ère Ethernet &amp; PROFINET</div>
            <p class="plan-desc">Infrastructure cuivre, 8 fils et switches. Déterminisme temps réel PROFINET (RT/IRT), adressage MAC/IP/Nom et synthèse globale.</p>
            <span class="plan-tag">Diapositives 17 à 22</span>
          </div>
        </div>
        ''',
        "notes": "Voici le plan de notre exposé. Nous commencerons par comprendre le besoin physique initial de simplification du câblage, avant de monter en abstraction vers les bus de terrain comme PROFIBUS, puis d'aborder la convergence Ethernet avec PROFINET."
    },

    # Slide 3: Remarque importante & Démarche
    {
        "id": 3,
        "section": "INTRODUCTION",
        "title": "Démarche pédagogique & Remarque liminaire",
        "subtitle": "Comprendre les principes fondamentaux plutôt que d'accumuler des catalogues de normes",
        "badge": "Méthodologie",
        "content": '''
        <div class="card alert-card">
          <div class="alert-header">
            <span class="alert-icon">💡</span>
            <span class="alert-title">Cadre de notre présentation</span>
          </div>
          <p class="lead-text">
            Cette présentation constitue une <strong>première approche structurée et conceptuelle</strong> des réseaux industriels.
            Ce domaine étant extrêmement vaste, hautement technique et en constante évolution, notre objectif n'est pas d'en mémoriser passivement chaque détail de norme, mais de :
          </p>
          <ul class="clean-list build-item">
            <li><strong>Comprendre la logique physique</strong> qui sous-tend les choix d'architecture (tensions, courants, signaux).</li>
            <li><strong>Démystifier le vocabulaire professionnel</strong> (RS-485, MBP, DP/PA, PROFINET RT, terminaisons actives).</li>
            <li><strong>Susciter votre curiosité d'ingénieur</strong> et vous donner les repères indispensables pour apprendre en autonomie.</li>
          </ul>
        </div>

        <div class="quote-card build-item">
          <div class="quote-mark">«</div>
          <div class="quote-body">
            <p class="quote-text">Le plus important n'est pas de tout connaître, mais de savoir où commencer à apprendre.</p>
          </div>
        </div>
        ''',
        "notes": "Avant d'entrer dans le détail technique, gardons à l'esprit cette citation. Dans notre métier d'automaticien, les protocoles évoluent sans cesse. L'important est de maîtriser les fondamentaux électriques et logiques pour être capable de s'adapter à n'importe quel réseau."
    },

    # Slide 4: Pourquoi les réseaux industriels ?
    {
        "id": 4,
        "section": "1. PROBLÉMATIQUE DU CÂBLAGE",
        "title": "Pourquoi les réseaux industriels ?",
        "subtitle": "De la multiplication des conducteurs à la communication numérique",
        "badge": "Problématique",
        "content": '''
        <div class="split-layout">
          <div class="col text-col" style="flex: 1.2;">
            <h3 class="section-heading">Les limites critiques du câblage traditionnel :</h3>
            <ul class="bullet-list">
              <li class="build-item"><strong>Liaison point à point systématique :</strong> chaque capteur ou bouton doit être raccordé par ses propres fils jusqu'au bornier de l'automate.</li>
              <li class="build-item"><strong>Saturation des armoires électriques :</strong> goulottes pleines à craquer, surchauffe et manque d'espace pour toute évolution.</li>
              <li class="build-item"><strong>Coûts de pose exorbitants :</strong> kilomètres de cuivre tirés, temps de repérage et de raccordement très lourd.</li>
              <li class="build-item"><strong>Dépannage fastidieux :</strong> identifier un conducteur coupé ou mal serré au milieu de centaines de brins demande des heures.</li>
              <li class="build-item"><strong>Risques de perturbations (CEM) :</strong> couplage capacitif et inductif néfaste entre câbles de puissance moteur et câbles de mesure analogique.</li>
            </ul>

            <div class="card curiosite-box build-item">
              <div class="curiosite-title">🔎 Petite curiosité pour réfléchir</div>
              <p>Imaginez une raffinerie ou une usine automobile comportant <strong>plus de 10 000 capteurs et actionneurs</strong> : faudrait-il raisonnablement tirer 10 000 câbles individuels de 200 mètres jusqu'à la salle de commande ?</p>
            </div>
          </div>

          <div class="col media-col" style="flex: 0.9;">
            <div class="img-frame">
              <img src="assets/image2.jpeg" alt="Armoire électrique traditionnelle saturée de fils" onerror="handleImgError(this)">
              <div class="caption">Exemple réel d'armoire traditionnelle : encombrement extrême et maintenance quasi impossible</div>
            </div>
          </div>
        </div>
        ''',
        "notes": "Regardez cette armoire électrique sur la droite. C'est ce qu'on appelle familièrement un plat de spaghettis. Chaque signal physique nécessitait sa propre paire de cuivre. Dès qu'un capteur tombait en panne, retrouver le bon fil relevait du défi."
    },

    # Slide 5: Avant / Après
    {
        "id": 5,
        "section": "1. PROBLÉMATIQUE DU CÂBLAGE",
        "title": "L'évolution : Avant / Après",
        "subtitle": "Le saut technologique : du faisceau fil-à-fil au câble de bus partagé",
        "badge": "La Solution",
        "content": '''
        <div class="avant-apres-container">
          <div class="svg-wrapper">
            ''' + get_svg_avant_apres() + '''
          </div>

          <div class="cards-duo">
            <div class="card before-card">
              <div class="duo-header red-text">✕ Câblage traditionnel</div>
              <div class="mini-img-wrap">
                <img src="assets/image3.jpeg" alt="Câblage point à point" onerror="handleImgError(this)">
              </div>
              <p>Faisceaux massifs de câbles, cuivre lourd, modifications matérielles coûteuses à chaque nouveau composant.</p>
            </div>

            <div class="card after-card">
              <div class="duo-header green-text">✓ Réseau en bus commun</div>
              <div class="mini-img-wrap">
                <img src="assets/image4.jpeg" alt="Câblage en bus propre" onerror="handleImgError(this)">
              </div>
              <p>Un seul câble multipoint reliant tous les équipements : réduction de 80% du câblage, diagnostic et flexibilité totale.</p>
            </div>
          </div>
        </div>
        ''',
        "notes": "Voici le saut qualitatif fondamental. À gauche, l'approche traditionnelle point-à-point : complexité en O de N. À droite, le bus de terrain : un seul câble deux fils chemine d'équipement en équipement. Non seulement on gagne du cuivre, mais on transporte des trames d'information riches avec des diagnostics d'état."
    },

    # Slide 6: Classification selon le type
    {
        "id": 6,
        "section": "2. CLASSIFICATIONS",
        "title": "Classification selon le type et le degré d'ouverture",
        "subtitle": "Comment les équipements et les constructeurs communiquent-ils entre eux ?",
        "badge": "Modèles de Réseaux",
        "content": '''
        <div class="three-cols">
          <div class="card type-card build-item">
            <div class="type-pill badge-specifique">1. Spécifique (Propriétaire)</div>
            <div class="img-frame-card">
              <img src="assets/image5.jpeg" alt="Réseau spécifique Fuji Electric" onerror="handleImgError(this)">
            </div>
            <h4 class="card-title">Système fermé</h4>
            <ul class="card-list">
              <li>Conçu pour une seule marque d'automates.</li>
              <li>Protocoles internes propriétaires (ex: anciens bus constructeur).</li>
              <li>Passerelles coûteuses requises pour communiquer avec d'autres marques.</li>
            </ul>
          </div>

          <div class="card type-card build-item">
            <div class="type-pill badge-homogene">2. Réseau Homogène</div>
            <div class="img-frame-card">
              <img src="assets/image6.jpeg" alt="Réseau homogène Siemens" onerror="handleImgError(this)">
            </div>
            <h4 class="card-title">Monoconstructeur</h4>
            <ul class="card-list">
              <li>Tous les équipements proviennent du même fabricant (ex: 100% Siemens).</li>
              <li>Configuration fluide et bibliothèques logicielles unifiées.</li>
              <li>Dépendance commerciale vis-à-vis du fournisseur unique.</li>
            </ul>
          </div>

          <div class="card type-card build-item">
            <div class="type-pill badge-heterogene">3. Réseau Hétérogène</div>
            <div class="img-frame-card">
              <img src="assets/image7.jpeg" alt="Réseau hétérogène multimarques" onerror="handleImgError(this)">
            </div>
            <h4 class="card-title">Standard ouvert (Interopérable)</h4>
            <ul class="card-list">
              <li>Cohabitation d'équipements de marques différentes (Siemens, Rockwell, Schneider, etc.).</li>
              <li>Repose sur des normes internationales (IEC 61158, IEEE 802.3).</li>
              <li>Liberté de choix du meilleur matériel pour chaque application.</li>
            </ul>
          </div>
        </div>
        ''',
        "notes": "Cette classification répond à la question stratégique : choisit-on une solution captive auprès d'un seul fournisseur, ou s'oriente-t-on vers des standards ouverts permettant de mixer des automates Siemens, des variateurs Rockwell et des vannes Fisher ?"
    },

    # Slide 7: Classification selon le niveau (Pyramide)
    {
        "id": 7,
        "section": "2. CLASSIFICATIONS",
        "title": "La Pyramide de l'automatisation industrielle",
        "subtitle": "Structuration en trois niveaux hiérarchiques, du capteur à l'usine",
        "badge": "Pyramide CIM",
        "content": '''
        <div class="split-layout">
          <div class="col svg-col" style="flex: 1.3;">
            <div class="svg-wrapper">
              ''' + get_svg_pyramide() + '''
            </div>
            <div class="card retenir-box" style="margin-top: 15px;">
              <span class="retenir-tag">À RETENIR</span>
              <p><strong>Type de réseau</strong> répond à : <em>Comment les constructeurs sont-ils organisés ?</em><br>
              <strong>Niveau de réseau</strong> répond à : <em>Où se situe l'échange de données dans l'usine ?</em></p>
            </div>
          </div>

          <div class="col cards-col" style="flex: 0.9;">
            <div class="level-card level-3 build-item">
              <div class="level-num">NIVEAU 3 · USINE</div>
              <div class="level-name">Supervision &amp; Conduite (SCADA / MES)</div>
              <p>Stations d'opérateurs, historiens de données, suivi de production. Trafic Ethernet TCP/IP, débit élevé, temps de cycle de l'ordre de la seconde.</p>
            </div>

            <div class="level-card level-2 build-item">
              <div class="level-num">NIVEAU 2 · ATELIER</div>
              <div class="level-name">Commande &amp; Cellule (PLC, IHM, Variateurs)</div>
              <p>Automates programmables (Siemens, Schneider), îlots de vannes, robots. Échanges déterministes et cycliques rapides (1 à 10 ms).</p>
            </div>

            <div class="level-card level-1 build-item">
              <div class="level-num">NIVEAU 1 · TERRAIN</div>
              <div class="level-name">Instrumentation physique (Capteurs / Actionneurs)</div>
              <p>Transmetteurs de pression, débit, température, positionneurs de vannes. Au contact direct de la matière, parfois en zone inflammable (ATEX).</p>
            </div>
          </div>
        </div>
        ''',
        "notes": "Voici la pyramide de l'automatisation. Observez bien la double flèche : en montant vers l'usine, le volume de données explose mais le temps de réponse est plus tolérant. En descendant vers le terrain, les volumes de données par cycle sont petits, mais la contrainte de temps réel et de sécurité électrique devient draconienne."
    },

    # Slide 8: Protocoles par niveau
    {
        "id": 8,
        "section": "2. CLASSIFICATIONS",
        "title": "Quels protocoles utilise-t-on à chaque niveau ?",
        "subtitle": "Panorama des technologies industrielles de référence",
        "badge": "Cartographie",
        "content": '''
        <div class="three-cols">
          <!-- Col 1: Terrain -->
          <div class="card proto-col build-item">
            <div class="proto-header field-header">
              <span class="proto-badge">NIVEAU TERRAIN</span>
              <div class="proto-subtitle">Capteurs &amp; Actionneurs</div>
            </div>
            <div class="proto-img-wrap">
              <img src="assets/image13.png" alt="Capteurs de terrain" onerror="handleImgError(this)">
            </div>
            <div class="proto-body">
              <div class="proto-section-title">Protocoles majeurs :</div>
              <ul class="badge-list">
                <li class="proto-chip chip-blue">PROFIBUS PA</li>
                <li class="proto-chip chip-dark">HART (4–20 mA)</li>
                <li class="proto-chip chip-yellow">AS-Interface (AS-i)</li>
                <li class="proto-chip chip-green">IO-Link</li>
                <li class="proto-chip chip-slate">FOUNDATION Fieldbus</li>
              </ul>
              <p class="proto-role"><strong>Rôle :</strong> Relier les instruments de mesure physiques et vannes aux cartes d'acquisition avec télé-alimentation.</p>
            </div>
          </div>

          <!-- Col 2: Atelier -->
          <div class="card proto-col build-item">
            <div class="proto-header control-header">
              <span class="proto-badge">NIVEAU ATELIER</span>
              <div class="proto-subtitle">Automates &amp; Machines</div>
            </div>
            <div class="proto-img-wrap">
              <img src="assets/image15.png" alt="Armoires d'automates PROFINET" onerror="handleImgError(this)">
            </div>
            <div class="proto-body">
              <div class="proto-section-title">Protocoles majeurs :</div>
              <ul class="badge-list">
                <li class="proto-chip chip-purple">PROFIBUS DP</li>
                <li class="proto-chip chip-green-dark">PROFINET (RT/IRT)</li>
                <li class="proto-chip chip-red">EtherNet/IP</li>
                <li class="proto-chip chip-orange">Modbus RTU / TCP</li>
                <li class="proto-chip chip-teal">EtherCAT</li>
              </ul>
              <p class="proto-role"><strong>Rôle :</strong> Assurer la synchronisation ultra-rapide et déterministe entre automates, variateurs et robots.</p>
            </div>
          </div>

          <!-- Col 3: Usine -->
          <div class="card proto-col build-item">
            <div class="proto-header plant-header">
              <span class="proto-badge">NIVEAU USINE</span>
              <div class="proto-subtitle">Supervision &amp; Gestion</div>
            </div>
            <div class="proto-img-wrap">
              <img src="assets/image16.jpeg" alt="Architecture d'usine SCADA MES" onerror="handleImgError(this)">
            </div>
            <div class="proto-body">
              <div class="proto-section-title">Protocoles majeurs :</div>
              <ul class="badge-list">
                <li class="proto-chip chip-navy">Ethernet Industriel TCP/IP</li>
                <li class="proto-chip chip-teal">OPC UA (Standard 4.0)</li>
                <li class="proto-chip chip-dark">Modbus TCP</li>
                <li class="proto-chip chip-purple">MQTT / REST (IIoT Cloud)</li>
              </ul>
              <p class="proto-role"><strong>Rôle :</strong> Conduite d'ensemble, archivage des historiques de production, connexion ERP et maintenance.</p>
            </div>
          </div>
        </div>
        ''',
        "notes": "Notez bien cette répartition. Sur le terrain, on retrouve PROFIBUS PA et AS-i pour les capteurs. Au niveau cellule d'atelier, PROFIBUS DP et PROFINET dominent pour cadencer les moteurs et automates. Au sommet, OPC UA et Ethernet TCP/IP unifient les serveurs SCADA et MES."
    },

    # Slide 9: PROFIBUS définition & frise
    {
        "id": 9,
        "section": "3. LES BUS DE TERRAIN : PROFIBUS",
        "title": "PROFIBUS : Définition & Frise historique",
        "subtitle": "Le bus de terrain le plus déployé dans l'industrie mondiale",
        "badge": "Historique",
        "content": '''
        <div class="split-layout">
          <div class="col text-col" style="flex: 1.15;">
            <div class="card def-box">
              <h3 class="def-title">Qu'est-ce que PROFIBUS ?</h3>
              <p class="lead-text">
                <strong>PROFIBUS</strong> (<em>PROcess FIeld BUS</em>) est un standard international ouvert (normé <strong>IEC 61158</strong> et <strong>IEC 61784</strong>) permettant d'interconnecter de manière numérique des automates programmables avec des capteurs, des actionneurs et des équipements de puissance.
              </p>
            </div>

            <div class="timeline-container">
              <div class="timeline-step build-item">
                <div class="timeline-year">1987</div>
                <div class="timeline-content">
                  <strong>Initiative fédérale en Allemagne</strong> : 21 entreprises industrielles (dont Siemens, Bosch, Klöckner-Moeller) et instituts de recherche s'unissent pour créer un standard ouvert.
                </div>
              </div>

              <div class="timeline-step build-item">
                <div class="timeline-year">1993</div>
                <div class="timeline-content">
                  <strong>Normalisation de PROFIBUS DP</strong> (<em>Decentralized Periphery</em>) : optimisation drastique pour les échanges rapides de données d'entrées/sorties en atelier.
                </div>
              </div>

              <div class="timeline-step build-item">
                <div class="timeline-year">1996</div>
                <div class="timeline-content">
                  <strong>Spécification de PROFIBUS PA</strong> (<em>Process Automation</em>) : extension pour les industries chimiques et pétrolières avec télé-alimentation et sécurité intrinsèque (ATEX).
                </div>
              </div>

              <div class="timeline-step build-item">
                <div class="timeline-year">Aujourd'hui</div>
                <div class="timeline-content">
                  <strong>Plus de 85 millions de nœuds installés</strong> à travers le monde : pilier incontournable de l'outil industriel moderne.
                </div>
              </div>
            </div>
          </div>

          <div class="col media-col" style="flex: 0.95;">
            <div class="img-frame">
              <img src="assets/image18.png" alt="Câble violet DP et câble bleu PA" onerror="handleImgError(this)">
              <div class="caption">La signature visuelle normalisée : câble violet pour PROFIBUS DP (RS-485), câble bleu pour PROFIBUS PA (MBP)</div>
            </div>
            <div class="img-frame" style="margin-top: 15px;">
              <img src="assets/image17.jpeg" alt="Hiérarchie des réseaux industriels" onerror="handleImgError(this)">
              <div class="caption">Positionnement des réseaux d'axes (Motion), de terrain (Field) et d'automates (Controller)</div>
            </div>
          </div>
        </div>
        ''',
        "notes": "PROFIBUS est né en Allemagne à la fin des années 80 pour casser les monopoles des bus propriétaires fermés. Il a donné naissance à deux variantes sœurs : DP pour la périphérie décentralisée rapide, et PA pour l'automatisation des procédés."
    },

    # Slide 10: PROFIBUS DP vs PA
    {
        "id": 10,
        "section": "3. LES BUS DE TERRAIN : PROFIBUS",
        "title": "PROFIBUS DP vs PROFIBUS PA : Deux mondes",
        "subtitle": "Deux variantes complémentaires conçues pour des contraintes environnementales opposées",
        "badge": "Comparatif Technique",
        "content": '''
        <div class="dp-pa-wrap">
          <div class="svg-wrapper">
            ''' + get_svg_dp_vs_pa() + '''
          </div>

          <div class="photos-duo">
            <div class="card mini-feature-card">
              <div class="feature-head purple-text">PROFIBUS DP (RS-485)</div>
              <div class="img-thumb-wrap">
                <img src="assets/image19.jpeg" alt="Connecteurs PROFIBUS DP" onerror="handleImgError(this)">
              </div>
              <p>Objectif : <strong>Vitesse maximale</strong> (jusqu'à 12 Mbit/s) pour synchroniser axes, robots et racks d'E/S en usine manufacturière.</p>
            </div>

            <div class="card mini-feature-card">
              <div class="feature-head blue-text">PROFIBUS PA (MBP)</div>
              <div class="img-thumb-wrap">
                <img src="assets/image20.jpeg" alt="Topologie PROFIBUS PA" onerror="handleImgError(this)">
              </div>
              <p>Objectif : <strong>Sécurité &amp; Télé-alimentation</strong> (31,25 kbit/s fixe) pour transmetteurs de pression/débit en atmosphère explosive.</p>
            </div>
          </div>
        </div>
        ''',
        "notes": "Voici la comparaison clé à retenir pour vos examens. DP privilégie la vitesse brute jusqu'à 12 Mégabits par seconde en milieu manufacturier. PA privilégie la sécurité intrinsèque et l'alimentation sur deux fils à vitesse fixe de 31,25 kilobits par seconde en milieu de procédé continu."
    },

    # Slide 11: RS-485 vs MBP (Signaux & Analogies)
    {
        "id": 11,
        "section": "3. LES BUS DE TERRAIN : PROFIBUS",
        "title": "RS-485 vs MBP : Principes physiques & Analogies",
        "subtitle": "Comprendre la différence fondamentale entre signal de tension et modulation de courant",
        "badge": "Couche Physique",
        "content": '''
        <div class="split-layout">
          <div class="col analogies-col" style="flex: 1;">
            <div class="card analogy-card build-item">
              <div class="analogy-head">
                <span class="analogy-icon">📞</span>
                <span class="analogy-title">Analogie RS-485 : La ligne téléphonique</span>
              </div>
              <p>Dans une ligne téléphonique filaire, les fils transportent la voix (un <strong>signal de tension</strong>), mais votre poste téléphonique ou combiné doit être branché sur une prise électrique pour fonctionner.</p>
              <div class="consequence-pill red-consequence">➔ En RS-485 : chaque capteur ou automate doit posséder sa propre alimentation 24V séparée !</div>
            </div>

            <div class="card analogy-card build-item">
              <div class="analogy-head">
                <span class="analogy-icon">🔌</span>
                <span class="analogy-title">Analogie MBP : Le câble USB moderne</span>
              </div>
              <p>Lorsque vous branchez votre smartphone en USB sur votre PC, le câble assure <strong>les deux fonctions en même temps</strong> : il alimente la batterie tout en transférant vos photos !</p>
              <div class="consequence-pill green-consequence">➔ En MBP : les deux seuls fils transportent l'énergie continue ET les données modulées (±9 mA).</div>
            </div>
          </div>

          <div class="col svg-col" style="flex: 1.35;">
            <div class="svg-wrapper">
              ''' + get_svg_signaux() + '''
            </div>
          </div>
        </div>
        ''',
        "notes": "Retenez bien ces deux images mentales simples : le RS-485 est comme une ligne téléphonique qui ne fait que transmettre l'information sans alimenter le récepteur ; le MBP est comme un câble USB qui apporte l'énergie nécessaire tout en faisant dialoguer le composant."
    },

    # Slide 12: Quand choisir DP ou PA
    {
        "id": 12,
        "section": "3. LES BUS DE TERRAIN : PROFIBUS",
        "title": "Quand choisir PROFIBUS DP ou PROFIBUS PA ?",
        "subtitle": "Exemples concrets d'application dans l'industrie",
        "badge": "Cas d'Usage",
        "content": '''
        <div class="split-layout">
          <!-- Case DP -->
          <div class="col card choice-card build-item" style="flex: 1; border-top: 5px solid #7E22CE;">
            <div class="choice-badge badge-dp">CHOISIR PROFIBUS DP</div>
            <h3 class="choice-title">Industrie Manufacturière &amp; Lignes Rapides</h3>
            <ul class="bullet-list-sm">
              <li>Lignes d'assemblage automobile, machines de conditionnement, convoyage de colis.</li>
              <li>Temps de cycle requis : <strong>&lt; 5 millisecondes</strong>.</li>
              <li>Exemple : Relier un automate <strong>Siemens S7-300 / S7-1500</strong> à des îlots d'entrées/sorties <strong>ET 200</strong>, des variateurs de vitesse et des codeurs d'axes.</li>
              <li>Milieu : armoire électrique climatisée ou atelier mécanique propre.</li>
            </ul>
            <div class="img-frame" style="margin-top: 15px;">
              <img src="assets/image21.jpeg" alt="Automate S7-300 et modules ET200 en PROFIBUS DP" onerror="handleImgError(this)">
              <div class="caption">Automate Siemens S7-300 raccordé à des E/S déportées par câble violet PROFIBUS DP</div>
            </div>
          </div>

          <!-- Case PA -->
          <div class="col card choice-card build-item" style="flex: 1; border-top: 5px solid #0284C7;">
            <div class="choice-badge badge-pa">CHOISIR PROFIBUS PA</div>
            <h3 class="choice-title">Industrie de Procédés Continus &amp; Chimie</h3>
            <ul class="bullet-list-sm">
              <li>Raffineries pétrolières, chimie, agroalimentaire, traitement de l'eau, silos à grains.</li>
              <li>Contrainte majeure : <strong>Sécurité intrinsèque (ATEX)</strong> — aucune étincelle possible.</li>
              <li>Exemple : Transmetteurs de pression différentielle, débitmètres électromagnétiques et positionneurs de vannes installés sur des cuves et réacteurs.</li>
              <li>Milieu : extérieur, poussières inflammables, atmosphères corrosives.</li>
            </ul>
            <div class="img-frame" style="margin-top: 15px;">
              <img src="assets/image22.jpeg" alt="Transmetteur Rosemount pour procédé sévère" onerror="handleImgError(this)">
              <div class="caption">Transmetteur Rosemount pour zone sévère : télé-alimenté par le bus PA 2 fils</div>
            </div>
          </div>
        </div>
        ''',
        "notes": "Face à un cahier des charges : si votre problème est la synchronisation rapide de moteurs d'un banc d'assemblage, choisissez DP. Si vous instrumentez une colonne de distillation de solvants inflammables à 800 mètres du local technique, PA s'impose."
    },

    # Slide 13: Câble DP & Connecteur DB9
    {
        "id": 13,
        "section": "3. LES BUS DE TERRAIN : PROFIBUS",
        "title": "Câble PROFIBUS DP et connecteur DB9",
        "subtitle": "La constitution matérielle robuste garantissant l'immunité industrielle",
        "badge": "Matériel",
        "content": '''
        <div class="split-layout">
          <div class="col text-col" style="flex: 1.1;">
            <div class="card detail-card build-item">
              <h4 class="card-title purple-text">Le câble PROFIBUS DP normalisé</h4>
              <ul class="clean-list">
                <li><strong>Gaine violette distinctive :</strong> identification visuelle immédiate dans les chemins de câbles.</li>
                <li><strong>Deux conducteurs rigides :</strong>
                  <ul>
                    <li><strong class="green-text">Fil A (vert)</strong> : conducteur de données RxD/TxD-N.</li>
                    <li><strong class="red-text">Fil B (rouge)</strong> : conducteur de données RxD/TxD-P.</li>
                  </ul>
                </li>
                <li><strong>Double blindage de haute efficacité :</strong> feuillard en aluminium + tresse dense en cuivre étamé pour repousser les rayonnements électromagnétiques des moteurs (CEM).</li>
              </ul>
            </div>

            <div class="card detail-card build-item" style="margin-top: 15px;">
              <h4 class="card-title">Le connecteur Sub-D 9 broches industriel</h4>
              <ul class="clean-list">
                <li>Boîtier métallique blindé assurant la <strong>reprise de masse à 360°</strong>.</li>
                <li>Bornes doubles : entrée câble (<strong>A1, B1</strong>) et sortie câble (<strong>A2, B2</strong>) pour chaînage direct sans dérivation en Té.</li>
                <li>Modèles coudés à 90°, 35°, prise pour console de programmation (PG) et variantes rondes M12 étanches IP67.</li>
              </ul>
            </div>
          </div>

          <div class="col media-col" style="flex: 1.1;">
            <div class="gallery-grid">
              <div class="gallery-item">
                <img src="assets/image23.jpeg" alt="Câble violet et deux connecteurs DB9" onerror="handleImgError(this)">
                <span class="gallery-label">Câble DP confectionné avec connecteurs DB9</span>
              </div>
              <div class="gallery-item">
                <img src="assets/image25.jpeg" alt="Intérieur du connecteur FastConnect" onerror="handleImgError(this)">
                <span class="gallery-label">Bornier interne A1/B1 et A2/B2 + commutateur</span>
              </div>
              <div class="gallery-item">
                <img src="assets/image26.jpeg" alt="Connecteur Siemens avec voyant" onerror="handleImgError(this)">
                <span class="gallery-label">Fenêtres d'inspection du raccordement</span>
              </div>
              <div class="gallery-item">
                <img src="assets/image27.png" alt="Différents types de connecteurs DP" onerror="handleImgError(this)">
                <span class="gallery-label">Variantes 90°, 35°, prise PG et M12 étanche</span>
              </div>
            </div>
          </div>
        </div>
        ''',
        "notes": "Voici les connecteurs que vous manipulerez en usine. Remarquez la double paire de bornes A1/B1 et A2/B2 à l'intérieur : elle permet de faire entrer le câble venant de la station précédente et de ressortir vers la suivante sans couper le blindage."
    },

    # Slide 14: Pourquoi 9 broches pour 2 fils ?
    {
        "id": 14,
        "section": "3. LES BUS DE TERRAIN : PROFIBUS",
        "title": "Pourquoi 9 broches pour seulement 2 fils ?",
        "subtitle": "Le secret technique de la terminaison active de bus",
        "badge": "Terminaison Active",
        "content": '''
        <div class="split-layout">
          <div class="col svg-col" style="flex: 1.35;">
            <div class="svg-wrapper">
              ''' + get_svg_db9() + '''
            </div>
          </div>

          <div class="col text-col" style="flex: 0.95;">
            <div class="card rule-card build-item">
              <div class="rule-title">⚡ La règle d'or de l'interrupteur ON / OFF</div>
              <p>Chaque connecteur DB9 intègre un petit levier de terminaison :</p>
              <ul class="rule-list">
                <li><span class="badge-on">ON</span> : impérativement sur le <strong>PREMIER</strong> et sur le <strong>DERNIER</strong> équipement du segment !</li>
                <li><span class="badge-off">OFF</span> : sur <strong>TOUS</strong> les équipements intermédiaires.</li>
              </ul>
              <div class="mini-img-wrap" style="margin-top: 10px;">
                <img src="assets/image29.png" alt="Schéma des interrupteurs ON OFF le long du bus" onerror="handleImgError(this)">
              </div>
            </div>

            <div class="card retenir-box build-item" style="margin-top: 15px;">
              <span class="retenir-tag">LE RÔLE DES RÉSISTANCES</span>
              <p>Le pont <strong>390 Ω – 220 Ω – 390 Ω</strong> alimenté en 5V (broches 6 et 5) évite la réflexion d'onde en bout de câble et maintient une tension de repos stable hors transmission.</p>
            </div>
          </div>
        </div>
        ''',
        "notes": "C'est une question classique de diagnostic industriel : pourquoi 9 broches ? Parce que les broches 6 et 5 fournissent le 5 Volts et la masse 0 Volt indispensables pour alimenter les résistances de polarisation intégrées au connecteur."
    },

    # Slide 15: 4-20 mA & Modules AI [À VÉRIFIER]
    {
        "id": 15,
        "section": "3. LES BUS DE TERRAIN : PROFIBUS",
        "title": "Le standard analogique 4–20 mA et modules AI",
        "subtitle": "La référence analogique historique face aux bus de terrain",
        "badge": "[À VÉRIFIER]",
        "content": '''
        <div class="split-layout">
          <div class="col text-col" style="flex: 1.15;">
            <div class="academic-check-badge">SYNTHÈSE TECHNIQUE [À VÉRIFIER]</div>

            <div class="card detail-card build-item">
              <h4 class="card-title">1. Pourquoi 4 à 20 mA et non pas 0 à 20 mA ?</h4>
              <ul class="bullet-list-sm">
                <li><strong>Le concept du « zéro vivant » (Live Zero) :</strong>
                  <ul>
                    <li><strong class="green-text">4 mA</strong> = 0% de la mesure (ex: cuve vide à 0 bar).</li>
                    <li><strong class="teal-text">20 mA</strong> = 100% de la mesure (ex: cuve pleine à 10 bar).</li>
                    <li><strong class="red-text">0 mA</strong> = <em>Anomalie immédiate !</em> (Fil coupé, capteur détruit ou alimentation coupée).</li>
                  </ul>
                </li>
                <li><strong>Insensibilité à la longueur :</strong> l'intensité du courant reste rigoureusement constante tout au long de la boucle, compensant les pertes de tension du câble.</li>
              </ul>
            </div>

            <div class="card detail-card build-item" style="margin-top: 15px;">
              <h4 class="card-title">2. Modules d'entrées analogiques (AI) &amp; Limites</h4>
              <p>Les cartes d'entrées analogiques (ex: <em>Siemens ET 200S AI</em>) intègrent une résistance de shunt de précision (souvent 250 Ω) convertissant le 4–20 mA en 1–5 V mesuré par le convertisseur CAN.</p>
              <div class="limit-box red-consequence" style="margin-top: 8px;">
                <strong>Limite face aux bus numériques :</strong> 1 paire de fils dédiée par capteur (câblage point à point lourd) et transmission d'une seule valeur scalaire, sans diagnostic distant.
              </div>
            </div>
          </div>

          <div class="col media-col" style="flex: 0.95;">
            <div class="img-frame">
              <img src="assets/image31.jpeg" alt="Module Siemens ET 200S Compact" onerror="handleImgError(this)">
              <div class="caption">Module compact Siemens ET 200S pour acquisition d'entrées/sorties</div>
            </div>
            <div class="img-frame" style="margin-top: 15px;">
              <img src="assets/image34.jpeg" alt="Transmetteur Siemens SITRANS P" onerror="handleImgError(this)">
              <div class="caption">Transmetteur de pression industriel SITRANS P avec tête de raccordement</div>
            </div>
          </div>
        </div>
        ''',
        "notes": "Avant les bus de terrain, le 4-20 milliampères était la norme universelle. Retenez bien le concept du zéro vivant à 4 milliampères qui permet à l'automate de distinguer immédiatement un réservoir vide d'un câble accidentellement arraché."
    },

    # Slide 16: Coupleur DP/PA & Architecture de liaison
    {
        "id": 16,
        "section": "3. LES BUS DE TERRAIN : PROFIBUS",
        "title": "Le coupleur DP/PA et l'architecture de liaison",
        "subtitle": "La passerelle transparente unissant vitesse d'atelier et sécurité de terrain",
        "badge": "Interconnexion",
        "content": '''
        <div class="interconnexion-container">
          <div class="svg-wrapper">
            ''' + get_svg_chaine_liaison() + '''
          </div>

          <div class="three-cols" style="margin-top: 15px;">
            <div class="card mini-feature-card build-item">
              <div class="feature-head">Module Coupleur DP/PA</div>
              <div class="img-thumb-wrap">
                <img src="assets/image33.jpeg" alt="Module Siemens DP/PA Coupler" onerror="handleImgError(this)">
              </div>
              <p>Convertit physiquement le signal RS-485 en modulation de courant MBP et injecte l'alimentation 24V sur le bus PA.</p>
            </div>

            <div class="card mini-feature-card build-item">
              <div class="feature-head">Boîte de Dérivation PA</div>
              <div class="img-thumb-wrap">
                <img src="assets/image36.jpeg" alt="Boîte Pepperl Fuchs FieldConnex" onerror="handleImgError(this)">
              </div>
              <p>Boîtier étanche IP67 (ex: Pepperl+Fuchs) permettant de connecter les instruments en dérivations courtes (Spurs).</p>
            </div>

            <div class="card mini-feature-card build-item">
              <div class="feature-head">Zone ATEX Sécurisée</div>
              <div class="img-thumb-wrap">
                <img src="assets/image37.png" alt="Dérivations vers transmetteurs" onerror="handleImgError(this)">
              </div>
              <p>Alimente transmetteurs de pression, température et débit sans aucun risque d'étincelle en zone inflammable.</p>
            </div>
          </div>
        </div>
        ''',
        "notes": "Le coupleur DP/PA est une merveille d'ingénierie : pour l'automate S7, les instruments de mesure PA apparaissent comme de simples périphériques DP ordinaires. Le coupleur gère en toute transparence le changement de vitesse et la télé-alimentation."
    },

    # Slide 17: Ethernet : la base
    {
        "id": 17,
        "section": "4. ETHERNET & PROFINET",
        "title": "Ethernet : La base des réseaux modernes",
        "subtitle": "Infrastructure physique, 8 conducteurs, paires torsadées et commutation",
        "badge": "Standard IEEE 802.3",
        "content": '''
        <div class="split-layout">
          <div class="col text-col" style="flex: 1.15;">
            <div class="card analogy-card build-item">
              <div class="analogy-head">
                <span class="analogy-icon">💻</span>
                <span class="analogy-title">L'analogie de la salle informatique</span>
              </div>
              <p>Imaginez trois ordinateurs dans une salle : reliés à un commutateur (<strong>switch</strong>) par des câbles Ethernet, ils s'échangent des fichiers librement. En usine, le principe est identique : l'automate, le pupitre IHM, le variateur et le PC SCADA dialoguent à travers cette même base Ethernet.</p>
            </div>

            <div class="card detail-card build-item" style="margin-top: 15px;">
              <h4 class="card-title">Anatomie d'un câble Ethernet cuivre</h4>
              <ul class="bullet-list-sm">
                <li><strong>8 conducteurs en cuivre</strong> organisés en <strong>4 paires torsadées</strong> (norme T568A / T568B).</li>
                <li><strong>Pourquoi torsader les paires ?</strong> Le pas de torsion régulier annule les champs électromagnétiques mutuels (diaphonie) et repousse les bruits extérieurs.</li>
                <li><strong>Le Switch industriel :</strong> filtre et aiguille les trames vers le port du bon destinataire grâce à sa table d'adresses MAC, éliminant les collisions des anciens concentrateurs (Hubs).</li>
              </ul>
            </div>
          </div>

          <div class="col media-col" style="flex: 0.95;">
            <div class="gallery-grid">
              <div class="gallery-item">
                <img src="assets/image39.jpeg" alt="Pince à sertir et connecteur RJ45 8 fils" onerror="handleImgError(this)">
                <span class="gallery-label">Connecteur RJ45 et repérage des 8 conducteurs</span>
              </div>
              <div class="gallery-item">
                <img src="assets/image43.jpeg" alt="Câble dénudé montrant les 4 paires torsadées" onerror="handleImgError(this)">
                <span class="gallery-label">Les 4 paires torsadées cuivrées blindées</span>
              </div>
              <div class="gallery-item">
                <img src="assets/image40.jpeg" alt="Switch avec câbles Ethernet jaunes" onerror="handleImgError(this)">
                <span class="gallery-label">Commutateur réseau (Switch) en baie de brassage</span>
              </div>
              <div class="gallery-item">
                <img src="assets/image42.jpeg" alt="Cordons Ethernet multicolores" onerror="handleImgError(this)">
                <span class="gallery-label">Brassage réseau haute densité</span>
              </div>
            </div>
          </div>
        </div>
        ''',
        "notes": "Ethernet est la technologie la plus universelle au monde. Mais attention : dans une usine, on ne peut pas utiliser un simple câble de salon. Il faut un câble blindé industriel résistant aux huiles, et des switches capables de commuter en quelques microsecondes."
    },

    # Slide 18: PROFINET : Ethernet industriel
    {
        "id": 18,
        "section": "4. ETHERNET & PROFINET",
        "title": "PROFINET : Ethernet adapté aux exigences de l'industrie",
        "subtitle": "Process Field Network : le déterminisme temps réel greffé sur le standard mondial",
        "badge": "Standard PI",
        "content": '''
        <div class="split-layout">
          <div class="col text-col" style="flex: 1.2;">
            <div class="card def-box">
              <h3 class="def-title">Qu'est-ce que PROFINET ?</h3>
              <p class="lead-text">
                <strong>PROFINET</strong> (<em>Process Field Network</em>) est le standard ouvert de communication industrielle basé sur Ethernet (<strong>IEC 61158 / IEC 61784</strong>), développé par Profibus &amp; Profinet International (PI).
              </p>
            </div>

            <div class="card detail-card build-item" style="margin-top: 15px;">
              <h4 class="card-title">Pourquoi Ethernet bureautique ne suffit-il pas seul ?</h4>
              <p>Dans un bureau, un temps de latence de 50 ms pour charger un document est inoffensif. Sur une chaîne de découpe laser ou un robot automobile, un retard de 2 ms provoque une collision catastrophique !</p>
              
              <div class="profinet-classes-grid">
                <div class="p-class-card">
                  <div class="p-class-name">PROFINET NRT</div>
                  <div class="p-class-spec">Non-Real-Time (10–100 ms)</div>
                  <p>Utilise la pile standard TCP/IP pour le paramétrage, les diagnostics et les serveurs web embarqués.</p>
                </div>
                <div class="p-class-card green-highlight">
                  <div class="p-class-name">PROFINET RT</div>
                  <div class="p-class-spec">Real-Time (&lt; 1 ms)</div>
                  <p>Bypasse les couches 3 et 4 pour injecter les données d'E/S directement dans la couche 2 Ethernet.</p>
                </div>
                <div class="p-class-card purple-highlight">
                  <div class="p-class-name">PROFINET IRT</div>
                  <div class="p-class-spec">Isochronous Real-Time (&lt; 1 µs)</div>
                  <p>Synchronisation matérielle au niveau switch pour asservissement d'axes et contrôle de mouvement critique.</p>
                </div>
              </div>
            </div>
          </div>

          <div class="col media-col" style="flex: 0.9;">
            <div class="img-frame">
              <img src="assets/image41.jpeg" alt="Switch Siemens SCALANCE X224 avec câbles verts PROFINET" onerror="handleImgError(this)">
              <div class="caption">Switch industriel Siemens SCALANCE X224 câblé avec des cordons verts PROFINET blindés</div>
            </div>
            <div class="card retenir-box build-item" style="margin-top: 15px;">
              <span class="retenir-tag">À RETENIR</span>
              <p><strong>Ethernet</strong> fournit l'infrastructure physique du réseau.<br>
              <strong>PROFINET</strong> fournit les mécanismes d'échanges déterministes temps réel.</p>
            </div>
          </div>
        </div>
        ''',
        "notes": "Voici la formule clé à retenir : Ethernet est l'autoroute physique, mais PROFINET est la voie prioritaire avec feux intelligents qui garantit que vos trames de moteurs et de capteurs arrivent sans jamais être bloquées par un téléchargement de fichier bureautique."
    },

    # Slide 19: Adresses : MAC, IP, Nom PROFINET, TCP/IP [À VÉRIFIER]
    {
        "id": 19,
        "section": "4. ETHERNET & PROFINET",
        "title": "Adressage industriel : MAC, IP & Nom PROFINET",
        "subtitle": "Comment un automate identifie-t-il infailliblement ses équipements sans configuration manuelle ?",
        "badge": "[À VÉRIFIER]",
        "content": '''
        <div class="split-layout">
          <div class="col svg-col" style="flex: 1.35;">
            <div class="academic-check-badge">COUCHE D'ADRESSAGE [À VÉRIFIER]</div>
            <div class="svg-wrapper">
              ''' + get_svg_pile_profinet() + '''
            </div>
          </div>

          <div class="col media-col" style="flex: 0.95;">
            <div class="img-frame">
              <img src="assets/image44.jpeg" alt="Architecture réseau PROFINET et usines reliées" onerror="handleImgError(this)">
              <div class="caption">Topologie industrielle PROFINET reliant usines A, B, C avec anneau fibre et switches</div>
            </div>
            <div class="card alert-card build-item" style="margin-top: 15px;">
              <div class="alert-header">
                <span class="alert-icon">🔄</span>
                <span class="alert-title">Le protocole DCP (Remplacement à chaud)</span>
              </div>
              <p>Lorsqu'un variateur ou module d'E/S tombe en panne, le technicien le remplace par un appareil neuf sorti du carton. Grâce au protocole <strong>DCP</strong>, le contrôleur détecte son nom et lui réinjecte automatiquement son adresse IP sans ouvrir un PC !</p>
            </div>
          </div>
        </div>
        ''',
        "notes": "En automatisme moderne, l'ingénieur ne manipule pas des adresses IP compliquées sur le terrain. Il nomme son équipement dans TIA Portal. Si le module grille, on le remplace, l'automate le reconnaît par son nom et reprogramme son adresse IP automatiquement."
    },

    # Slide 20: Architecture industrielle complète
    {
        "id": 20,
        "section": "5. SYNTHÈSE GLOBALE",
        "title": "Architecture industrielle complète : Du capteur à l'ERP",
        "subtitle": "L'intégration verticale de l'Usine 4.0",
        "badge": "Vision Globale",
        "content": '''
        <div class="arch-complete-wrap">
          <div class="svg-wrapper">
            ''' + get_svg_architecture_complete() + '''
          </div>

          <div class="synthesis-footer-bar">
            <div class="footer-step-card">
              <span class="step-badge-mini blue-bg">Procédé (PA)</span>
              <span>Télé-alimentation 2 fils &amp; Sécurité ATEX</span>
            </div>
            <div class="step-arrow-mini">➔</div>
            <div class="footer-step-card">
              <span class="step-badge-mini purple-bg">Atelier (DP)</span>
              <span>RS-485 rapide (1,5 Mbaud) vers E/S déportées</span>
            </div>
            <div class="step-arrow-mini">➔</div>
            <div class="footer-step-card">
              <span class="step-badge-mini green-bg">Cellule (PROFINET)</span>
              <span>Temps réel déterministe &lt; 1 ms en anneau</span>
            </div>
            <div class="step-arrow-mini">➔</div>
            <div class="footer-step-card">
              <span class="step-badge-mini navy-bg">Usine (SCADA / ERP)</span>
              <span>Supervision Ethernet TCP/IP &amp; Base de données</span>
            </div>
          </div>
        </div>
        ''',
        "notes": "Voici la synthèse magistrale de notre présentation. Une mesure de pression prise par un transmetteur PA sur une cuve chimique est télé-alimentée en zone ATEX, convertie par le coupleur, acquise en temps réel par l'automate en PROFINET, visualisée par l'opérateur sur le SCADA, et archivée dans l'ERP."
    },

    # Slide 21: Conclusion générale
    {
        "id": 21,
        "section": "5. SYNTHÈSE GLOBALE",
        "title": "Conclusion : Ce que nous avons appris",
        "subtitle": "Les quatre piliers de la communication industrielle moderne",
        "badge": "Bilan Académique",
        "content": '''
        <div class="four-pillars-grid">
          <div class="pillar-card build-item">
            <div class="pillar-icon">1</div>
            <h4 class="pillar-title">Fin du fouillis de câbles</h4>
            <p>La transition du point-à-point vers les réseaux en bus partagés a permis d'économiser 80% de cuivre, de fiabiliser les installations et d'introduire le diagnostic numérique temps réel.</p>
          </div>

          <div class="pillar-card build-item">
            <div class="pillar-icon">2</div>
            <h4 class="pillar-title">Duo complémentaire DP / PA</h4>
            <p>PROFIBUS DP optimise la vitesse pure (RS-485) en atelier manufacturier, tandis que PROFIBUS PA garantit la télé-alimentation 2 fils et la sécurité intrinsèque (MBP) en zone dangereuse.</p>
          </div>

          <div class="pillar-card build-item">
            <div class="pillar-icon">3</div>
            <h4 class="pillar-title">Rigueur de l'infrastructure</h4>
            <p>Le bon fonctionnement repose sur des règles physiques strictes : terminaison active 220 Ω aux deux seules extrémités, reprise de blindage à 360° et passerelle coupleur DP/PA transparente.</p>
          </div>

          <div class="pillar-card build-item">
            <div class="pillar-icon">4</div>
            <h4 class="pillar-title">Convergence Ethernet &amp; IIoT</h4>
            <p>PROFINET unifie l'atelier sur le standard Ethernet universel sans sacrifier le temps réel (&lt; 1 ms), ouvrant la voie vers l'Industrie 4.0, OPC UA et les capteurs Ethernet-APL de demain.</p>
          </div>
        </div>

        <div class="card alert-card build-item" style="margin-top: 25px;">
          <div class="alert-header">
            <span class="alert-icon">🚀</span>
            <span class="alert-title">Perspectives d'avenir : L'Ethernet-APL</span>
          </div>
          <p>La toute dernière frontière technologique s'appelle <strong>Ethernet-APL</strong> (<em>Advanced Physical Layer</em>) : elle amène le protocole Ethernet standard directement sur 2 fils télé-alimentés jusqu'aux capteurs en zone explosive à 10 Mbit/s !</p>
        </div>
        ''',
        "notes": "En conclusion : nous avons vu comment l'automatisation a réussi à faire converger le monde physique de l'électricité avec le monde informatique des réseaux. L'avenir s'oriente vers un protocole unique, du capteur de cuve jusqu'au cloud de gestion."
    },

    # Slide 22: Questions & Débat / Remerciements
    {
        "id": 22,
        "section": "CONCLUSION",
        "title": "Questions & Échanges avec la classe",
        "subtitle": "Merci pour votre attention active !",
        "badge": "Discussion",
        "content": '''
        <div class="split-layout">
          <div class="col text-col" style="flex: 1.2;">
            <div class="quote-card" style="margin-bottom: 25px;">
              <div class="quote-mark">«</div>
              <div class="quote-body">
                <p class="quote-text">Le plus important n'est pas de tout connaître, mais de savoir où commencer à apprendre.</p>
              </div>
            </div>

            <div class="card intro-meta-box">
              <h3 class="def-title" style="margin-bottom: 15px;">Séance de questions / réponses ouverte :</h3>
              <ul class="bullet-list-sm">
                <li>Des questions sur le fonctionnement du codage Manchester ou du RS-485 ?</li>
                <li>Des interrogations sur le dimensionnement des terminaisons de bus ?</li>
                <li>Des remarques sur le passage de PROFIBUS à PROFINET dans vos futurs projets ?</li>
              </ul>
            </div>

            <div class="nav-hint-pill" style="margin-top: 20px;">
              Présentation réalisée par <strong class="editable-name" contenteditable="true" spellcheck="false">[NOM]</strong> · Novembre 2026
            </div>
          </div>

          <div class="col media-col" style="flex: 0.95;">
            <div class="img-frame">
              <img src="assets/image46.png" alt="Schéma d'intégration des réseaux industriels" onerror="handleImgError(this)">
              <div class="caption">Rappel de l'intégration globale : Internet / Entreprise ➔ PROFINET ➔ PROFIBUS DP ➔ PROFIBUS PA</div>
            </div>
          </div>
        </div>
        ''',
        "notes": "Je vous remercie très chaleureusement pour votre écoute. Je suis désormais à votre entière disposition pour répondre à toutes vos questions ou revenir sur l'un des schémas techniques de la présentation."
    }
]

# Generate Slide HTML
slides_html = ""
overview_cards_html = ""

for s in slides:
    slide_id = s["id"]
    active_class = "active" if slide_id == 1 else ""
    slides_html += f'''
    <!-- Slide {slide_id} -->
    <section class="slide {active_class}" id="slide-{slide_id}" data-slide-index="{slide_id}" data-section="{s['section']}">
      <div class="slide-header">
        <div class="header-left">
          <span class="section-tag">{s['section']}</span>
          <h2 class="slide-title">{s['title']}</h2>
          <div class="slide-subtitle">{s['subtitle']}</div>
        </div>
        <div class="header-right">
          <span class="badge-pill">{s['badge']}</span>
        </div>
      </div>
      <div class="slide-body">
        {s['content']}
      </div>
    </section>
    '''

    overview_cards_html += f'''
    <div class="overview-card" onclick="goToSlide({slide_id})">
      <div class="ov-num">{slide_id}</div>
      <div class="ov-sec">{s['section']}</div>
      <div class="ov-title">{s['title']}</div>
      <div class="ov-badge">{s['badge']}</div>
    </div>
    '''

notes_json = json.dumps({s["id"]: {"title": s["title"], "notes": s["notes"]} for s in slides}, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Les Réseaux Industriels — Présentation Académique</title>
  <style>
    /* ==========================================================================
       CSS STYLES - STANDALONE ACADEMIC PRESENTATION (PROJECTOR-OPTIMIZED)
       ========================================================================== */
    :root {{
      --bg-canvas: #FAFAF7;
      --bg-card: #FFFFFF;
      --text-main: #1B1F24;
      --text-muted: #374151;
      --primary-navy: #1F3A5F;
      --primary-navy-dark: #12243C;
      --accent-teal: #2A7F8E;
      --accent-teal-light: #EBF7F8;
      --amber-alert: #C98A1B;
      --amber-bg: #FEF8ED;
      --border-subtle: #E2E8F0;
      --border-strong: #CBD5E1;
      --shadow-card: 0 4px 14px rgba(0, 0, 0, 0.06);
      --shadow-elevated: 0 12px 28px rgba(0, 0, 0, 0.12);
      --dp-purple: #7E22CE;
      --pa-blue: #0284C7;
      --pn-green: #15803D;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html, body {{
      width: 100%;
      height: 100%;
      overflow: hidden;
      background-color: #121418;
      font-family: system-ui, -apple-system, "Segoe UI", Calibri, Roboto, sans-serif;
      color: var(--text-main);
      -webkit-font-smoothing: antialiased;
    }}

    /* Presentation Screen Stage - Fixed 1920x1080 canvas scaled to viewport */
    #viewport-container {{
      width: 100vw;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      position: relative;
    }}

    #presentation-stage {{
      width: 1920px;
      height: 1080px;
      background-color: var(--bg-canvas);
      position: absolute;
      transform-origin: center center;
      display: flex;
      flex-direction: column;
      box-shadow: 0 0 40px rgba(0,0,0,0.4);
      user-select: text;
    }}

    /* Top Progress Bar */
    #top-progress-track {{
      width: 100%;
      height: 6px;
      background: #E2E8F0;
      position: relative;
      z-index: 50;
    }}
    #top-progress-bar {{
      height: 100%;
      width: 4.54%;
      background: linear-gradient(90deg, var(--primary-navy), var(--accent-teal));
      transition: width 280ms ease-out;
    }}

    /* Global Header */
    #stage-header {{
      height: 52px;
      padding: 0 60px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(4px);
    }}
    .stage-header-title {{
      font-family: Georgia, serif;
      font-size: 17px;
      font-weight: 700;
      color: var(--primary-navy);
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    .stage-header-section {{
      font-size: 15px;
      font-weight: 600;
      color: var(--accent-teal);
    }}

    /* Slide Deck Container */
    #slide-deck {{
      flex: 1;
      position: relative;
      overflow: hidden;
      width: 100%;
      height: calc(1080px - 52px - 60px - 6px);
    }}

    /* Each Slide */
    .slide {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      padding: 35px 65px 25px 65px;
      display: none;
      flex-direction: column;
      opacity: 0;
      transform: translateX(18px);
      transition: opacity 260ms ease, transform 260ms ease;
    }}

    .slide.active {{
      display: flex;
      opacity: 1;
      transform: translateX(0);
      z-index: 10;
    }}

    /* Slide Header Area */
    .slide-header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      margin-bottom: 24px;
      padding-bottom: 14px;
      border-bottom: 2px solid var(--border-subtle);
      position: relative;
    }}
    .slide-header::after {{
      content: "";
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 120px;
      height: 3px;
      background: var(--accent-teal);
    }}

    .section-tag {{
      display: inline-block;
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      color: var(--accent-teal);
      margin-bottom: 4px;
    }}
    .slide-title {{
      font-family: Georgia, Cambria, "Times New Roman", serif;
      font-size: 42px;
      font-weight: 700;
      color: var(--primary-navy);
      line-height: 1.15;
    }}
    .slide-subtitle {{
      font-size: 21px;
      color: var(--text-muted);
      margin-top: 4px;
      font-weight: 400;
    }}

    .badge-pill {{
      display: inline-block;
      padding: 6px 16px;
      border-radius: 20px;
      background: var(--accent-teal-light);
      color: var(--accent-teal);
      font-size: 14px;
      font-weight: 700;
      border: 1px solid rgba(42, 127, 142, 0.25);
    }}

    /* Slide Body Area */
    .slide-body {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      position: relative;
    }}

    /* Footer Bar */
    #stage-footer {{
      height: 60px;
      padding: 0 60px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border-subtle);
      background: #FFFFFF;
      font-size: 16px;
      color: var(--text-muted);
      z-index: 50;
    }}
    .footer-left {{
      font-weight: 600;
      color: var(--primary-navy);
    }}
    .footer-center {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .footer-right {{
      display: flex;
      align-items: center;
      gap: 20px;
      font-weight: 600;
    }}
    .counter-badge {{
      background: #F1F5F9;
      padding: 4px 14px;
      border-radius: 12px;
      border: 1px solid var(--border-subtle);
      color: var(--primary-navy);
      font-weight: 700;
      font-size: 16px;
    }}

    .editable-name {{
      display: inline-block;
      padding: 2px 8px;
      background: #FEF3C7;
      color: #92400E;
      border-radius: 4px;
      border: 1px dashed #D97706;
      cursor: text;
      font-weight: 700;
      min-width: 80px;
      outline: none;
    }}
    .editable-name:focus {{
      background: #FDE68A;
      border-style: solid;
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.25);
    }}

    /* On-Screen Navigation Controls */
    .screen-controls {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .btn-nav {{
      background: #FFFFFF;
      border: 1px solid var(--border-strong);
      color: var(--primary-navy);
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 150ms ease;
    }}
    .btn-nav:hover {{
      background: var(--accent-teal);
      color: #FFFFFF;
      border-color: var(--accent-teal);
      transform: translateY(-1px);
    }}

    /* Side Chevron Click Targets */
    .side-nav-zone {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 50px;
      height: 90px;
      background: rgba(31, 58, 95, 0.12);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--primary-navy);
      font-size: 24px;
      cursor: pointer;
      opacity: 0.2;
      transition: opacity 150ms ease, background 150ms ease;
      z-index: 60;
    }}
    .side-nav-zone:hover {{
      opacity: 1;
      background: rgba(31, 58, 95, 0.85);
      color: #FFFFFF;
    }}
    .side-nav-prev {{ left: 8px; }}
    .side-nav-next {{ right: 8px; }}

    /* Layout Primitives */
    .split-layout {{
      display: flex;
      gap: 40px;
      align-items: center;
      width: 100%;
      height: 100%;
    }}
    .col {{
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}
    .three-cols {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
      width: 100%;
      height: 100%;
      align-items: stretch;
    }}

    /* Card Component */
    .card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 24px 28px;
      box-shadow: var(--shadow-card);
    }}

    /* Alert / Revenir Boxes */
    .alert-card {{
      border-left: 6px solid var(--accent-teal);
      background: #F8FDFF;
    }}
    .retenir-box {{
      border-left: 6px solid var(--amber-alert);
      background: var(--amber-bg);
      border-color: #FCD34D;
      padding: 18px 24px;
    }}
    .retenir-tag {{
      display: inline-block;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 1px;
      color: #92400E;
      background: #FDE68A;
      padding: 3px 10px;
      border-radius: 6px;
      margin-bottom: 8px;
    }}
    .curiosite-box {{
      border: 2px dashed var(--amber-alert);
      background: #FFFBEB;
      padding: 18px 22px;
      margin-top: 15px;
    }}
    .curiosite-title {{
      font-family: Georgia, serif;
      font-size: 18px;
      font-weight: bold;
      color: #92400E;
      margin-bottom: 6px;
    }}

    /* Image Frames & Fallbacks */
    .img-frame {{
      background: #FFFFFF;
      border: 1px solid var(--border-strong);
      border-radius: 10px;
      padding: 10px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .img-frame img {{
      max-width: 100%;
      max-height: 480px;
      width: auto;
      height: auto;
      object-fit: contain;
      border-radius: 6px;
      display: block;
    }}
    .caption {{
      margin-top: 8px;
      font-size: 14px;
      font-weight: 600;
      color: #475569;
      text-align: center;
      line-height: 1.35;
    }}

    .img-fallback-box {{
      width: 100%;
      min-height: 220px;
      background: #F8FAFC;
      border: 2px dashed #94A3B8;
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px;
      color: #475569;
    }}
    .fallback-icon {{ font-size: 40px; margin-bottom: 8px; }}
    .fallback-text {{ font-size: 16px; font-weight: bold; text-align: center; }}

    /* Typography & Lists */
    .main-title {{
      font-family: Georgia, serif;
      font-size: 58px;
      font-weight: 800;
      color: var(--primary-navy);
      line-height: 1.1;
      margin-bottom: 12px;
    }}
    .sub-title {{
      font-size: 28px;
      font-weight: 600;
      color: var(--accent-teal);
      margin-bottom: 15px;
      line-height: 1.25;
    }}
    .baseline {{
      font-size: 22px;
      color: var(--text-muted);
      margin-bottom: 25px;
      line-height: 1.35;
    }}
    .lead-text {{
      font-size: 23px;
      line-height: 1.45;
      color: var(--text-main);
      margin-bottom: 14px;
    }}
    .academic-badge {{
      display: inline-block;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: var(--primary-navy);
      background: #E2E8F0;
      padding: 4px 14px;
      border-radius: 6px;
      margin-bottom: 16px;
    }}

    .bullet-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 14px;
      font-size: 22px;
      line-height: 1.4;
    }}
    .bullet-list li {{
      position: relative;
      padding-left: 32px;
    }}
    .bullet-list li::before {{
      content: "▪";
      position: absolute;
      left: 6px;
      top: -2px;
      color: var(--accent-teal);
      font-size: 28px;
    }}

    .bullet-list-sm {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 18px;
      line-height: 1.4;
    }}
    .bullet-list-sm li {{
      position: relative;
      padding-left: 24px;
    }}
    .bullet-list-sm li::before {{
      content: "•";
      position: absolute;
      left: 4px;
      color: var(--accent-teal);
      font-size: 22px;
    }}

    .clean-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 19px;
      line-height: 1.4;
    }}
    .clean-list li {{
      position: relative;
      padding-left: 24px;
    }}
    .clean-list li::before {{
      content: "➔";
      position: absolute;
      left: 0;
      color: var(--accent-teal);
      font-size: 15px;
      top: 2px;
    }}

    /* Quote Card */
    .quote-card {{
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-left: 6px solid var(--primary-navy);
      border-radius: 12px;
      padding: 24px 30px;
      display: flex;
      align-items: center;
      gap: 20px;
      margin-top: 25px;
      box-shadow: var(--shadow-card);
    }}
    .quote-mark {{
      font-family: Georgia, serif;
      font-size: 70px;
      line-height: 0.6;
      color: var(--accent-teal);
      opacity: 0.5;
    }}
    .quote-text {{
      font-family: Georgia, serif;
      font-size: 25px;
      font-style: italic;
      color: var(--primary-navy);
      line-height: 1.35;
    }}

    /* Plan Grid */
    .plan-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
      width: 100%;
      height: 100%;
      align-content: center;
    }}
    .plan-card {{
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 26px 30px;
      box-shadow: var(--shadow-card);
      position: relative;
      transition: transform 180ms ease, border-color 180ms ease;
    }}
    .plan-card:hover {{
      transform: translateY(-3px);
      border-color: var(--accent-teal);
    }}
    .plan-num {{
      font-family: Georgia, serif;
      font-size: 38px;
      font-weight: 800;
      color: var(--accent-teal);
      line-height: 1;
      margin-bottom: 8px;
    }}
    .plan-title {{
      font-family: Georgia, serif;
      font-size: 26px;
      font-weight: 700;
      color: var(--primary-navy);
      margin-bottom: 8px;
    }}
    .plan-desc {{
      font-size: 18px;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 12px;
    }}
    .plan-tag {{
      display: inline-block;
      font-size: 13px;
      font-weight: 700;
      padding: 3px 10px;
      background: #F1F5F9;
      color: var(--primary-navy);
      border-radius: 6px;
    }}

    /* Timeline Steps */
    .timeline-container {{
      display: flex;
      flex-direction: column;
      gap: 14px;
      margin-top: 15px;
    }}
    .timeline-step {{
      display: flex;
      gap: 16px;
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 12px 18px;
      align-items: center;
    }}
    .timeline-year {{
      font-family: Georgia, serif;
      font-size: 20px;
      font-weight: 800;
      color: var(--dp-purple);
      min-width: 90px;
    }}
    .timeline-content {{
      font-size: 17px;
      line-height: 1.35;
      color: var(--text-main);
    }}

    /* SVG Containers */
    .svg-wrapper {{
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
    .academic-svg {{
      max-width: 100%;
      height: auto;
      max-height: 480px;
      display: block;
    }}

    /* Gallery Grid */
    .gallery-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
      width: 100%;
    }}
    .gallery-item {{
      background: #FFFFFF;
      border: 1px solid var(--border-strong);
      border-radius: 8px;
      padding: 8px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .gallery-item img {{
      max-width: 100%;
      max-height: 180px;
      object-fit: contain;
      border-radius: 4px;
    }}
    .gallery-label {{
      font-size: 12px;
      font-weight: 600;
      color: #475569;
      margin-top: 6px;
    }}

    /* Special Pills & Badges */
    .academic-check-badge {{
      display: inline-block;
      padding: 4px 12px;
      background: #FEF3C7;
      color: #92400E;
      border: 1px solid #F59E0B;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 1px;
      border-radius: 4px;
      margin-bottom: 10px;
    }}

    .green-text {{ color: #15803D !important; }}
    .red-text {{ color: #DC2626 !important; }}
    .purple-text {{ color: #7E22CE !important; }}
    .blue-text {{ color: #0284C7 !important; }}
    .teal-text {{ color: #0D9488 !important; }}

    .badge-on {{
      background: #DC2626;
      color: #FFFFFF;
      padding: 3px 10px;
      border-radius: 4px;
      font-weight: 800;
      font-size: 13px;
    }}
    .badge-off {{
      background: #475569;
      color: #FFFFFF;
      padding: 3px 10px;
      border-radius: 4px;
      font-weight: 800;
      font-size: 13px;
    }}

    .badge-dp {{
      background: #FAF5FF;
      color: #7E22CE;
      border: 1px solid #C084FC;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      display: inline-block;
      margin-bottom: 8px;
    }}
    .badge-pa {{
      background: #F0F9FF;
      color: #0284C7;
      border: 1px solid #7DD3FC;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      display: inline-block;
      margin-bottom: 8px;
    }}

    .profinet-classes-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-top: 12px;
    }}
    .p-class-card {{
      background: #F8FAFC;
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 12px;
      font-size: 14px;
    }}
    .p-class-name {{
      font-family: Georgia, serif;
      font-weight: bold;
      font-size: 15px;
      margin-bottom: 4px;
    }}
    .p-class-spec {{
      font-size: 12px;
      font-weight: bold;
      color: #64748B;
      margin-bottom: 6px;
    }}
    .green-highlight {{
      background: #F0FDF4;
      border-color: #86EFAC;
    }}
    .purple-highlight {{
      background: #FAF5FF;
      border-color: #D8B4FE;
    }}

    /* Four Pillars Grid (Conclusion) */
    .four-pillars-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      width: 100%;
    }}
    .pillar-card {{
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 22px;
      box-shadow: var(--shadow-card);
      position: relative;
    }}
    .pillar-icon {{
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: var(--primary-navy);
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: Georgia, serif;
      font-weight: bold;
      font-size: 18px;
      margin-bottom: 12px;
    }}
    .pillar-title {{
      font-family: Georgia, serif;
      font-size: 20px;
      font-weight: bold;
      color: var(--primary-navy);
      margin-bottom: 10px;
    }}
    .pillar-card p {{
      font-size: 16px;
      line-height: 1.45;
      color: var(--text-muted);
    }}

    /* Bottom Architecture Bar (Slide 20) */
    .synthesis-footer-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-top: 15px;
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 12px 20px;
    }}
    .footer-step-card {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 14px;
      font-weight: 600;
    }}
    .step-badge-mini {{
      padding: 4px 10px;
      border-radius: 6px;
      color: #FFFFFF;
      font-size: 12px;
      font-weight: bold;
    }}
    .blue-bg {{ background: var(--pa-blue); }}
    .purple-bg {{ background: var(--dp-purple); }}
    .green-bg {{ background: var(--pn-green); }}
    .navy-bg {{ background: var(--primary-navy); }}
    .step-arrow-mini {{
      color: #94A3B8;
      font-weight: bold;
    }}

    /* Build Animation (one-by-one bullets) */
    .build-item {{
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 240ms ease, transform 240ms ease;
    }}
    .build-item.revealed {{
      opacity: 1;
      transform: translateY(0);
    }}

    /* Modals (Overview O & Notes S) */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(5px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
    }}
    .modal-overlay.open {{
      display: flex;
    }}

    .modal-box {{
      background: #FFFFFF;
      border-radius: 14px;
      box-shadow: var(--shadow-elevated);
      max-width: 90vw;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    /* Overview Modal */
    #overview-modal .modal-box {{
      width: 1400px;
      height: 820px;
    }}
    .modal-header {{
      padding: 18px 28px;
      background: var(--primary-navy);
      color: #FFFFFF;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .modal-header h3 {{
      font-family: Georgia, serif;
      font-size: 22px;
      font-weight: bold;
    }}
    .modal-close-btn {{
      background: none;
      border: none;
      color: #FFFFFF;
      font-size: 26px;
      cursor: pointer;
      line-height: 1;
    }}
    .overview-grid {{
      flex: 1;
      padding: 24px;
      overflow-y: auto;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      background: #F8FAFC;
    }}
    .overview-card {{
      background: #FFFFFF;
      border: 2px solid var(--border-subtle);
      border-radius: 8px;
      padding: 16px;
      cursor: pointer;
      transition: all 150ms ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 125px;
    }}
    .overview-card:hover {{
      border-color: var(--accent-teal);
      transform: translateY(-2px);
      box-shadow: 0 6px 14px rgba(0,0,0,0.08);
    }}
    .overview-card.current {{
      border-color: var(--dp-purple);
      background: #FAF5FF;
    }}
    .ov-num {{
      font-family: Georgia, serif;
      font-size: 22px;
      font-weight: 800;
      color: var(--accent-teal);
    }}
    .ov-sec {{
      font-size: 11px;
      font-weight: 700;
      color: #64748B;
      text-transform: uppercase;
    }}
    .ov-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--primary-navy);
      line-height: 1.25;
    }}
    .ov-badge {{
      font-size: 11px;
      font-weight: 600;
      color: #0284C7;
    }}

    /* Notes Modal */
    #notes-modal .modal-box {{
      width: 680px;
      max-height: 520px;
    }}
    .notes-content-wrap {{
      padding: 24px 28px;
      overflow-y: auto;
    }}
    .notes-slide-title {{
      font-family: Georgia, serif;
      font-size: 20px;
      font-weight: bold;
      color: var(--primary-navy);
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .notes-body {{
      font-size: 20px;
      line-height: 1.5;
      color: #1E293B;
      background: #F1F5F9;
      border-left: 5px solid var(--accent-teal);
      padding: 16px 20px;
      border-radius: 6px;
    }}

    /* Help Modal */
    #help-modal .modal-box {{
      width: 580px;
    }}
    .help-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 14px;
      font-size: 16px;
    }}
    .help-table td {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .help-table td:first-child {{
      font-weight: bold;
      color: var(--primary-navy);
      width: 40%;
    }}

    /* Reduced Motion */
    @media (prefers-reduced-motion: reduce) {{
      .slide, .build-item, #top-progress-bar {{
        transition: none !important;
        transform: none !important;
      }}
    }}

    /* Print Stylesheet (PDF Export 1 slide per page) */
    @media print {{
      @page {{
        size: 16in 9in;
        margin: 0;
      }}
      html, body {{
        width: 100% !important;
        height: auto !important;
        overflow: visible !important;
        background: #FFFFFF !important;
      }}
      #viewport-container {{
        width: 100% !important;
        height: auto !important;
        display: block !important;
      }}
      #presentation-stage {{
        position: static !important;
        transform: none !important;
        width: 100% !important;
        height: auto !important;
        box-shadow: none !important;
      }}
      #top-progress-track, #stage-header, #stage-footer, .side-nav-zone, .modal-overlay {{
        display: none !important;
      }}
      #slide-deck {{
        height: auto !important;
        position: static !important;
      }}
      .slide {{
        display: flex !important;
        opacity: 1 !important;
        transform: none !important;
        position: relative !important;
        width: 100vw !important;
        height: 100vh !important;
        page-break-after: always !important;
        break-after: page !important;
        padding: 40px !important;
      }}
      .build-item {{
        opacity: 1 !important;
        transform: none !important;
      }}
    }}
  </style>
</head>
<body>
  <div id="viewport-container">
    <div id="presentation-stage">
      
      <!-- Top Progress Bar -->
      <div id="top-progress-track">
        <div id="top-progress-bar"></div>
      </div>

      <!-- Stage Header -->
      <header id="stage-header">
        <div class="stage-header-title">LES RÉSEAUX INDUSTRIELS</div>
        <div class="stage-header-section" id="current-section-name">1. INTRODUCTION GÉNÉRALE</div>
      </header>

      <!-- Side Quick Nav Targets -->
      <div class="side-nav-zone side-nav-prev" onclick="stepPrev()" title="Diapositive précédente (←)">◀</div>
      <div class="side-nav-zone side-nav-next" onclick="stepNext()" title="Diapositive suivante (→)">▶</div>

      <!-- Slide Deck -->
      <main id="slide-deck">
        {slides_html}
      </main>

      <!-- Stage Footer -->
      <footer id="stage-footer">
        <div class="footer-left">Les réseaux industriels · Automatisme &amp; Informatique industrielle</div>
        <div class="footer-center">
          <span>Présenté par :</span>
          <span class="editable-name" contenteditable="true" spellcheck="false" title="Cliquez pour éditer votre nom">[NOM]</span>
        </div>
        <div class="footer-right">
          <div class="screen-controls">
            <button class="btn-nav" onclick="toggleOverview()" title="Vue d'ensemble en miniatures (Touche O)">⊞ Grille</button>
            <button class="btn-nav" onclick="toggleNotes()" title="Notes du présentateur (Touche S)">📝 Notes</button>
            <button class="btn-nav" onclick="toggleFullscreen()" title="Plein écran (Touche F)">⛶ Plein écran</button>
            <button class="btn-nav" onclick="toggleHelp()" title="Raccourcis clavier (Touche H ou ?)">❓ Aide</button>
          </div>
          <div class="counter-badge">
            <span id="current-slide-num">1</span> / <span id="total-slides-num">22</span>
          </div>
        </div>
      </footer>

    </div>
  </div>

  <!-- Overview Modal (O) -->
  <div class="modal-overlay" id="overview-modal" onclick="handleOverlayClick(event, 'overview-modal')">
    <div class="modal-box">
      <div class="modal-header">
        <h3>Vue d'ensemble de la présentation (22 Diapositives)</h3>
        <button class="modal-close-btn" onclick="toggleOverview()">&times;</button>
      </div>
      <div class="overview-grid">
        {overview_cards_html}
      </div>
    </div>
  </div>

  <!-- Notes Modal (S) -->
  <div class="modal-overlay" id="notes-modal" onclick="handleOverlayClick(event, 'notes-modal')">
    <div class="modal-box">
      <div class="modal-header">
        <h3>Notes de présentation (À dire à l'oral)</h3>
        <button class="modal-close-btn" onclick="toggleNotes()">&times;</button>
      </div>
      <div class="notes-content-wrap">
        <div class="notes-slide-title" id="notes-slide-title">Titre de la diapositive</div>
        <div class="notes-body" id="notes-text">Notes orales du présentateur...</div>
      </div>
    </div>
  </div>

  <!-- Help Modal (H) -->
  <div class="modal-overlay" id="help-modal" onclick="handleOverlayClick(event, 'help-modal')">
    <div class="modal-box">
      <div class="modal-header">
        <h3>Raccourcis clavier de la présentation</h3>
        <button class="modal-close-btn" onclick="toggleHelp()">&times;</button>
      </div>
      <div class="notes-content-wrap">
        <table class="help-table">
          <tr><td>Flèche Droite (→), Espace, PgDown</td><td>Avancer (point par point ou diapo suivante)</td></tr>
          <tr><td>Flèche Gauche (←), PgUp</td><td>Reculer (point par point ou diapo précédente)</td></tr>
          <tr><td>Touche F</td><td>Basculer en mode Plein écran</td></tr>
          <tr><td>Touche O</td><td>Ouvrir la grille de miniatures (vue d'ensemble)</td></tr>
          <tr><td>Touche S</td><td>Afficher les notes orales du présentateur</td></tr>
          <tr><td>Touche Home / End</td><td>Aller à la première / dernière diapositive</td></tr>
          <tr><td>Touche Échap (Esc)</td><td>Fermer les fenêtres modales / Quitter le plein écran</td></tr>
          <tr><td>Touche H / ?</td><td>Afficher cette aide</td></tr>
        </table>
      </div>
    </div>
  </div>

  <script>
    /* ==========================================================================
       JAVASCRIPT CONTROLLER - POWERPOINT-LIKE AUTONOMOUS SLIDE ENGINE
       ========================================================================== */
    const TOTAL_SLIDES = 22;
    let currentSlide = 1;
    const speakerNotes = {notes_json};

    // Stage Auto-scaling to 16:9 viewport
    function updateStageScale() {{
      const stage = document.getElementById('presentation-stage');
      if (!stage) return;
      const vw = window.innerWidth;
      const vh = window.innerHeight;
      const scale = Math.min(vw / 1920, vh / 1080);
      stage.style.transform = `scale(${{scale}})`;
    }}

    window.addEventListener('resize', updateStageScale);
    window.addEventListener('DOMContentLoaded', () => {{
      updateStageScale();
      initSlideFromHash();
      initEditableName();
      setupTouchSwipe();
    }});

    // Name persistence in localStorage
    function initEditableName() {{
      const savedName = localStorage.getItem('presenter_name');
      const nameElements = document.querySelectorAll('.editable-name');
      if (savedName) {{
        nameElements.forEach(el => el.textContent = savedName);
      }}
      nameElements.forEach(el => {{
        el.addEventListener('input', () => {{
          const val = el.textContent;
          nameElements.forEach(other => {{ if (other !== el) other.textContent = val; }});
          localStorage.setItem('presenter_name', val);
        }});
      }});
    }}

    // Fallback if image fails
    function handleImgError(img) {{
      img.style.display = 'none';
      const fallback = document.createElement('div');
      fallback.className = 'img-fallback-box';
      fallback.innerHTML = `<div class="fallback-icon">📷</div><div class="fallback-text">Image : ${{img.alt || 'Illustration technique'}}</div>`;
      if (img.parentNode) {{
        img.parentNode.insertBefore(fallback, img);
      }}
    }}

    // Navigation logic with build-items (bullet points)
    function goToSlide(index, revealAllBuilds = false) {{
      if (index < 1) index = 1;
      if (index > TOTAL_SLIDES) index = TOTAL_SLIDES;

      const prevSlideEl = document.querySelector('.slide.active');
      if (prevSlideEl) {{
        prevSlideEl.classList.remove('active');
      }}

      currentSlide = index;
      const nextSlideEl = document.getElementById(`slide-${{currentSlide}}`);
      if (nextSlideEl) {{
        nextSlideEl.classList.add('active');
        
        // Handle build items
        const builds = nextSlideEl.querySelectorAll('.build-item');
        builds.forEach(b => {{
          if (revealAllBuilds) {{
            b.classList.add('revealed');
          }} else {{
            b.classList.remove('revealed');
          }}
        }});

        // Update header & footer
        const sec = nextSlideEl.getAttribute('data-section') || '';
        document.getElementById('current-section-name').textContent = sec;
        document.getElementById('current-slide-num').textContent = currentSlide;

        // Update progress bar
        const progressPct = ((currentSlide - 1) / (TOTAL_SLIDES - 1)) * 100;
        document.getElementById('top-progress-bar').style.width = `${{Math.max(4, progressPct)}}%`;

        // Update URL hash without polluting history
        history.replaceState(null, null, `#${{currentSlide}}`);

        // Update speaker notes if modal is open
        updateNotesContent();

        // Update active card in overview
        document.querySelectorAll('.overview-card').forEach((card, idx) => {{
          if (idx + 1 === currentSlide) {{
            card.classList.add('current');
          }} else {{
            card.classList.remove('current');
          }}
        }});
      }}
    }}

    function stepNext() {{
      const currentEl = document.getElementById(`slide-${{currentSlide}}`);
      if (currentEl) {{
        const nextBuild = currentEl.querySelector('.build-item:not(.revealed)');
        if (nextBuild) {{
          nextBuild.classList.add('revealed');
          return;
        }}
      }}
      if (currentSlide < TOTAL_SLIDES) {{
        goToSlide(currentSlide + 1, false);
      }}
    }}

    function stepPrev() {{
      const currentEl = document.getElementById(`slide-${{currentSlide}}`);
      if (currentEl) {{
        const revealedBuilds = currentEl.querySelectorAll('.build-item.revealed');
        if (revealedBuilds.length > 0) {{
          revealedBuilds[revealedBuilds.length - 1].classList.remove('revealed');
          return;
        }}
      }}
      if (currentSlide > 1) {{
        goToSlide(currentSlide - 1, true);
      }}
    }}

    function initSlideFromHash() {{
      const hash = window.location.hash.replace('#', '');
      const parsed = parseInt(hash, 10);
      if (!isNaN(parsed) && parsed >= 1 && parsed <= TOTAL_SLIDES) {{
        goToSlide(parsed);
      }} else {{
        goToSlide(1);
      }}
    }}

    // Keyboard events
    window.addEventListener('keydown', (e) => {{
      // Don't intercept when editing name
      if (document.activeElement && document.activeElement.isContentEditable) {{
        return;
      }}

      switch(e.key) {{
        case 'ArrowRight':
        case ' ':
        case 'PageDown':
          e.preventDefault();
          stepNext();
          break;
        case 'ArrowLeft':
        case 'PageUp':
          e.preventDefault();
          stepPrev();
          break;
        case 'Home':
          e.preventDefault();
          goToSlide(1);
          break;
        case 'End':
          e.preventDefault();
          goToSlide(TOTAL_SLIDES);
          break;
        case 'f':
        case 'F':
          e.preventDefault();
          toggleFullscreen();
          break;
        case 'o':
        case 'O':
          e.preventDefault();
          toggleOverview();
          break;
        case 's':
        case 'S':
          e.preventDefault();
          toggleNotes();
          break;
        case 'h':
        case 'H':
        case '?':
          e.preventDefault();
          toggleHelp();
          break;
        case 'Escape':
          closeAllModals();
          break;
      }}
    }});

    // Modals
    function toggleOverview() {{
      const m = document.getElementById('overview-modal');
      m.classList.toggle('open');
    }}

    function toggleNotes() {{
      const m = document.getElementById('notes-modal');
      m.classList.toggle('open');
      if (m.classList.contains('open')) {{
        updateNotesContent();
      }}
    }}

    function toggleHelp() {{
      const m = document.getElementById('help-modal');
      m.classList.toggle('open');
    }}

    function closeAllModals() {{
      document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('open'));
    }}

    function handleOverlayClick(e, modalId) {{
      if (e.target.id === modalId) {{
        document.getElementById(modalId).classList.remove('open');
      }}
    }}

    function updateNotesContent() {{
      const data = speakerNotes[currentSlide];
      if (data) {{
        document.getElementById('notes-slide-title').textContent = `Diapo ${{currentSlide}} : ${{data.title}}`;
        document.getElementById('notes-text').textContent = data.notes;
      }}
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => {{
          console.warn('Plein écran non disponible :', err);
        }});
      }} else {{
        if (document.exitFullscreen) {{
          document.exitFullscreen();
        }}
      }}
    }}

    // Touch Swipe Detection
    function setupTouchSwipe() {{
      let touchStartX = 0;
      let touchStartY = 0;
      const stage = document.getElementById('presentation-stage');

      stage.addEventListener('touchstart', (e) => {{
        touchStartX = e.changedTouches[0].screenX;
        touchStartY = e.changedTouches[0].screenY;
      }}, {{ passive: true }});

      stage.addEventListener('touchend', (e) => {{
        const diffX = e.changedTouches[0].screenX - touchStartX;
        const diffY = e.changedTouches[0].screenY - touchStartY;
        if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 40) {{
          if (diffX < 0) {{
            stepNext();
          }} else {{
            stepPrev();
          }}
        }}
      }}, {{ passive: true }});
    }}
  </script>
</body>
</html>
'''

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Presentation generated successfully at: {target_file}")
print(f"File size: {os.path.getsize(target_file):,} bytes")
