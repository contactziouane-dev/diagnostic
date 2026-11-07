# -*- coding: utf-8 -*-
"""
Generator for the standalone academic presentation 'LES RÉSEAUX INDUSTRIELS'.
Generates a complete, offline-ready index.html with inline SVG diagrams,
slide scaling, speaker notes, grid overview, and print support.
"""

import os
import json

def get_svg_pyramide():
    return '''<svg viewBox="0 0 900 460" class="academic-svg" aria-label="Pyramide de l'automatisation à 3 niveaux">
  <defs>
    <linearGradient id="gradTop" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1F3A5F"/>
      <stop offset="100%" stop-color="#2D5584"/>
    </linearGradient>
    <linearGradient id="gradMid" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2A7F8E"/>
      <stop offset="100%" stop-color="#38A3A5"/>
    </linearGradient>
    <linearGradient id="gradBot" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E4B56"/>
      <stop offset="100%" stop-color="#166678"/>
    </linearGradient>
    <filter id="shadowPyramid" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.15"/>
    </filter>
  </defs>

  <!-- Left Arrow: Data Volume -->
  <g transform="translate(45, 230)">
    <line x1="0" y1="180" x2="0" y2="-180" stroke="#1F3A5F" stroke-width="3" stroke-dasharray="4,4"/>
    <polygon points="0,-190 -8,-172 8,-172" fill="#1F3A5F"/>
    <text x="-15" y="0" font-family="'Segoe UI', Calibri, sans-serif" font-size="15" font-weight="700" fill="#1F3A5F" text-anchor="middle" transform="rotate(-90 -15 0)">VOLUME DE DONNÉES CROISSANT</text>
  </g>

  <!-- Right Arrow: Real-Time Criticality -->
  <g transform="translate(855, 230)">
    <line x1="0" y1="-180" x2="0" y2="180" stroke="#C98A1B" stroke-width="3" stroke-dasharray="4,4"/>
    <polygon points="0,190 -8,172 8,172" fill="#C98A1B"/>
    <text x="20" y="0" font-family="'Segoe UI', Calibri, sans-serif" font-size="15" font-weight="700" fill="#C98A1B" text-anchor="middle" transform="rotate(90 20 0)">DÉTERMINISME &amp; CONTRAINTES TEMPS RÉEL</text>
  </g>

  <!-- Top Tier: Usine / Supervision -->
  <g filter="url(#shadowPyramid)">
    <polygon points="450,20 330,140 570,140" fill="url(#gradTop)" stroke="#FFFFFF" stroke-width="2"/>
    <text x="450" y="65" font-family="Georgia, serif" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">NIVEAU 3 · USINE</text>
    <text x="450" y="87" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="600" fill="#E2E8F0" text-anchor="middle">SUPERVISION &amp; GESTION (SCADA / MES / ERP)</text>
    <rect x="365" y="100" width="170" height="24" rx="12" fill="rgba(255,255,255,0.18)"/>
    <text x="450" y="117" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">Ethernet TCP/IP · OPC UA</text>
  </g>

  <!-- Middle Tier: Atelier / Contrôle -->
  <g filter="url(#shadowPyramid)">
    <polygon points="325,148 205,278 695,278 575,148" fill="url(#gradMid)" stroke="#FFFFFF" stroke-width="2"/>
    <text x="450" y="185" font-family="Georgia, serif" font-size="20" font-weight="bold" fill="#FFFFFF" text-anchor="middle">NIVEAU 2 · ATELIER</text>
    <text x="450" y="210" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="600" fill="#F0FDFA" text-anchor="middle">COMMANDE &amp; COORDINATION (PLC, IHM, Variateurs, Robots)</text>
    <g transform="translate(260, 225)">
      <rect x="0" y="0" width="175" height="30" rx="6" fill="#FFFFFF" opacity="0.95"/>
      <text x="87" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#1F3A5F" text-anchor="middle">PROFIBUS DP (RS-485)</text>
    </g>
    <g transform="translate(465, 225)">
      <rect x="0" y="0" width="175" height="30" rx="6" fill="#FFFFFF" opacity="0.95"/>
      <text x="87" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#15803D" text-anchor="middle">PROFINET (RT / IRT)</text>
    </g>
  </g>

  <!-- Bottom Tier: Terrain / Procédé -->
  <g filter="url(#shadowPyramid)">
    <polygon points="200,286 75,426 825,426 700,286" fill="url(#gradBot)" stroke="#FFFFFF" stroke-width="2"/>
    <text x="450" y="325" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#FFFFFF" text-anchor="middle">NIVEAU 1 · TERRAIN</text>
    <text x="450" y="352" font-family="'Segoe UI', Calibri, sans-serif" font-size="15" font-weight="600" fill="#CCFBF1" text-anchor="middle">INSTRUMENTATION &amp; ACTIONNEMENT (Capteurs, Transmetteurs, Vannes)</text>
    
    <g transform="translate(130, 372)">
      <rect x="0" y="0" width="140" height="32" rx="6" fill="#0284C7"/>
      <text x="70" y="21" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">PROFIBUS PA</text>
    </g>
    <g transform="translate(290, 372)">
      <rect x="0" y="0" width="130" height="32" rx="6" fill="#334155"/>
      <text x="65" y="21" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4–20 mA / HART</text>
    </g>
    <g transform="translate(440, 372)">
      <rect x="0" y="0" width="130" height="32" rx="6" fill="#EAB308"/>
      <text x="65" y="21" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#1E293B" text-anchor="middle">AS-Interface</text>
    </g>
    <g transform="translate(590, 372)">
      <rect x="0" y="0" width="140" height="32" rx="6" fill="#059669"/>
      <text x="70" y="21" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">IO-Link / FF</text>
    </g>
  </g>
</svg>'''

def get_svg_avant_apres():
    return '''<svg viewBox="0 0 920 380" class="academic-svg" aria-label="Schéma comparatif point à point versus réseau bus">
  <!-- Left Box: Avant Point à Point -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="435" height="355" rx="12" fill="#FFF5F5" stroke="#F87171" stroke-width="2"/>
    <rect x="0" y="0" width="435" height="42" rx="12" fill="#DC2626"/>
    <text x="217" y="27" font-family="Georgia, serif" font-size="17" font-weight="bold" fill="#FFFFFF" text-anchor="middle">AVANT : CÂBLAGE POINT À POINT</text>
    
    <!-- PLC Block -->
    <rect x="30" y="65" width="85" height="230" rx="6" fill="#1F3A5F" stroke="#0F172A" stroke-width="2"/>
    <text x="72" y="170" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle" transform="rotate(-90 72 170)">AUTOMATE (PLC)</text>
    
    <!-- Tangled Cables -->
    <path d="M 115 85 C 220 85, 180 90, 310 90" stroke="#DC2626" stroke-width="2.5" fill="none"/>
    <path d="M 115 110 C 230 110, 170 130, 310 130" stroke="#EA580C" stroke-width="2.5" fill="none"/>
    <path d="M 115 135 C 210 160, 240 170, 310 170" stroke="#CA8A04" stroke-width="2.5" fill="none"/>
    <path d="M 115 160 C 250 140, 190 210, 310 210" stroke="#16A34A" stroke-width="2.5" fill="none"/>
    <path d="M 115 185 C 200 230, 250 250, 310 250" stroke="#0284C7" stroke-width="2.5" fill="none"/>
    <path d="M 115 210 C 220 200, 200 280, 310 285" stroke="#9333EA" stroke-width="2.5" fill="none"/>

    <!-- Field Devices -->
    <g transform="translate(315, 75)">
      <rect x="0" y="0" width="95" height="30" rx="4" fill="#FFFFFF" stroke="#DC2626" stroke-width="1.5"/>
      <text x="47" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="600" fill="#1E293B" text-anchor="middle">Capteur 1</text>
    </g>
    <g transform="translate(315, 115)">
      <rect x="0" y="0" width="95" height="30" rx="4" fill="#FFFFFF" stroke="#EA580C" stroke-width="1.5"/>
      <text x="47" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="600" fill="#1E293B" text-anchor="middle">Capteur 2</text>
    </g>
    <g transform="translate(315, 155)">
      <rect x="0" y="0" width="95" height="30" rx="4" fill="#FFFFFF" stroke="#CA8A04" stroke-width="1.5"/>
      <text x="47" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="600" fill="#1E293B" text-anchor="middle">Vanne 1</text>
    </g>
    <g transform="translate(315, 195)">
      <rect x="0" y="0" width="95" height="30" rx="4" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.5"/>
      <text x="47" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="600" fill="#1E293B" text-anchor="middle">Capteur 3</text>
    </g>
    <g transform="translate(315, 235)">
      <rect x="0" y="0" width="95" height="30" rx="4" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
      <text x="47" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="600" fill="#1E293B" text-anchor="middle">Vanne 2</text>
    </g>
    <g transform="translate(315, 272)">
      <rect x="0" y="0" width="95" height="30" rx="4" fill="#FFFFFF" stroke="#9333EA" stroke-width="1.5"/>
      <text x="47" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="600" fill="#1E293B" text-anchor="middle">Moteur 1</text>
    </g>

    <!-- Legend -->
    <text x="217" y="335" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#991B1B" text-anchor="middle">⚠ 1 câble par signal · Armoires saturées · Dépannage lourd</text>
  </g>

  <!-- Right Box: Après Réseau Bus -->
  <g transform="translate(475, 10)">
    <rect x="0" y="0" width="435" height="355" rx="12" fill="#F0FDF4" stroke="#4ADE80" stroke-width="2"/>
    <rect x="0" y="0" width="435" height="42" rx="12" fill="#16A34A"/>
    <text x="217" y="27" font-family="Georgia, serif" font-size="17" font-weight="bold" fill="#FFFFFF" text-anchor="middle">APRÈS : COMMUNICATION EN RÉSEAU BUS</text>

    <!-- PLC Block -->
    <rect x="25" y="65" width="85" height="230" rx="6" fill="#1F3A5F" stroke="#0F172A" stroke-width="2"/>
    <text x="67" y="170" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle" transform="rotate(-90 67 170)">AUTOMATE (PLC)</text>

    <!-- Single Bus Line (Purple DP or Blue PA) -->
    <line x1="110" y1="180" x2="385" y2="180" stroke="#7E22CE" stroke-width="6" stroke-linecap="round"/>
    <text x="245" y="170" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#7E22CE" text-anchor="middle">CÂBLE BUS COMMUN (2 fils blindés)</text>

    <!-- Tap drops (Spurs) to devices -->
    <line x1="165" y1="180" x2="165" y2="115" stroke="#7E22CE" stroke-width="3"/>
    <line x1="245" y1="180" x2="245" y2="115" stroke="#7E22CE" stroke-width="3"/>
    <line x1="325" y1="180" x2="325" y2="115" stroke="#7E22CE" stroke-width="3"/>

    <line x1="165" y1="180" x2="165" y2="245" stroke="#7E22CE" stroke-width="3"/>
    <line x1="245" y1="180" x2="245" y2="245" stroke="#7E22CE" stroke-width="3"/>
    <line x1="325" y1="180" x2="325" y2="245" stroke="#7E22CE" stroke-width="3"/>

    <!-- Nodes Top -->
    <g transform="translate(125, 75)">
      <rect x="0" y="0" width="80" height="40" rx="5" fill="#FFFFFF" stroke="#16A34A" stroke-width="2"/>
      <text x="40" y="24" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">Capteur 1</text>
    </g>
    <g transform="translate(205, 75)">
      <rect x="0" y="0" width="80" height="40" rx="5" fill="#FFFFFF" stroke="#16A34A" stroke-width="2"/>
      <text x="40" y="24" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">Capteur 2</text>
    </g>
    <g transform="translate(285, 75)">
      <rect x="0" y="0" width="80" height="40" rx="5" fill="#FFFFFF" stroke="#16A34A" stroke-width="2"/>
      <text x="40" y="24" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">Vanne 1</text>
    </g>

    <!-- Nodes Bottom -->
    <g transform="translate(125, 245)">
      <rect x="0" y="0" width="80" height="40" rx="5" fill="#FFFFFF" stroke="#16A34A" stroke-width="2"/>
      <text x="40" y="24" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">Capteur 3</text>
    </g>
    <g transform="translate(205, 245)">
      <rect x="0" y="0" width="80" height="40" rx="5" fill="#FFFFFF" stroke="#16A34A" stroke-width="2"/>
      <text x="40" y="24" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">Vanne 2</text>
    </g>
    <g transform="translate(285, 245)">
      <rect x="0" y="0" width="80" height="40" rx="5" fill="#FFFFFF" stroke="#16A34A" stroke-width="2"/>
      <text x="40" y="24" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">Moteur 1</text>
    </g>

    <!-- Terminator at end -->
    <circle cx="385" cy="180" r="7" fill="#DC2626"/>
    <text x="385" y="205" font-family="'Segoe UI', Calibri, sans-serif" font-size="10" font-weight="bold" fill="#DC2626" text-anchor="middle">Terminaison</text>

    <!-- Legend -->
    <text x="217" y="335" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#15803D" text-anchor="middle">✓ Un seul câble · Diagnostic numérique · Ajout immédiat</text>
  </g>
</svg>'''

def get_svg_dp_vs_pa():
    return '''<svg viewBox="0 0 920 380" class="academic-svg" aria-label="Tableau comparatif PROFIBUS DP versus PA">
  <defs>
    <filter id="shadowTable" x="-2%" y="-2%" width="104%" height="106%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Table Header -->
  <rect x="20" y="10" width="260" height="50" rx="8" fill="#1F3A5F"/>
  <text x="150" y="40" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">CARACTÉRISTIQUE</text>

  <rect x="290" y="10" width="300" height="50" rx="8" fill="#7E22CE"/>
  <text x="440" y="40" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">PROFIBUS DP (Decentralized Periphery)</text>

  <rect x="600" y="10" width="300" height="50" rx="8" fill="#0284C7"/>
  <text x="750" y="40" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">PROFIBUS PA (Process Automation)</text>

  <!-- Row 1: Couche physique -->
  <g transform="translate(20, 68)">
    <rect x="0" y="0" width="260" height="42" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="20" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#1E293B">Couche physique</text>

    <rect x="270" y="0" width="300" height="42" fill="#FAF5FF" stroke="#E9D5FF"/>
    <text x="420" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#6B21A8" text-anchor="middle">RS-485 (Différentiel de tension)</text>

    <rect x="580" y="0" width="300" height="42" fill="#F0F9FF" stroke="#BAE6FD"/>
    <text x="730" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#0369A1" text-anchor="middle">MBP (Manchester Bus Powered)</text>
  </g>

  <!-- Row 2: Vitesse / Débit -->
  <g transform="translate(20, 116)">
    <rect x="0" y="0" width="260" height="42" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="20" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#1E293B">Vitesse de transmission</text>

    <rect x="270" y="0" width="300" height="42" fill="#FAF5FF" stroke="#E9D5FF"/>
    <text x="420" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#6B21A8" text-anchor="middle">9,6 kbit/s jusqu'à 12 Mbit/s (Rapide)</text>

    <rect x="580" y="0" width="300" height="42" fill="#F0F9FF" stroke="#BAE6FD"/>
    <text x="730" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#0369A1" text-anchor="middle">Fixe : 31,25 kbit/s (Déterministe)</text>
  </g>

  <!-- Row 3: Télé-alimentation -->
  <g transform="translate(20, 164)">
    <rect x="0" y="0" width="260" height="42" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="20" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#1E293B">Alimentation des capteurs</text>

    <rect x="270" y="0" width="300" height="42" fill="#FAF5FF" stroke="#E9D5FF"/>
    <text x="420" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#B91C1C" text-anchor="middle">Séparée (Alimentation 24V externe)</text>

    <rect x="580" y="0" width="300" height="42" fill="#F0F9FF" stroke="#BAE6FD"/>
    <text x="730" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#15803D" text-anchor="middle">Sur le bus (Données + 24V sur 2 fils)</text>
  </g>

  <!-- Row 4: Câble & Couleur -->
  <g transform="translate(20, 212)">
    <rect x="0" y="0" width="260" height="42" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="20" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#1E293B">Câble standardisé</text>

    <rect x="270" y="0" width="300" height="42" fill="#FAF5FF" stroke="#E9D5FF"/>
    <text x="420" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#6B21A8" text-anchor="middle">Violet blindé (Fil A vert, B rouge)</text>

    <rect x="580" y="0" width="300" height="42" fill="#F0F9FF" stroke="#BAE6FD"/>
    <text x="730" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#0369A1" text-anchor="middle">Bleu blindé (Zones Ex) ou Noir</text>
  </g>

  <!-- Row 5: Topologie -->
  <g transform="translate(20, 260)">
    <rect x="0" y="0" width="260" height="42" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="20" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#1E293B">Topologie réseau</text>

    <rect x="270" y="0" width="300" height="42" fill="#FAF5FF" stroke="#E9D5FF"/>
    <text x="420" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#6B21A8" text-anchor="middle">Ligne pure avec terminaisons actives</text>

    <rect x="580" y="0" width="300" height="42" fill="#F0F9FF" stroke="#BAE6FD"/>
    <text x="730" y="26" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#0369A1" text-anchor="middle">Tronc (Trunk) + Dérivations (Spurs)</text>
  </g>

  <!-- Row 6: Domaine d'application -->
  <g transform="translate(20, 308)">
    <rect x="0" y="0" width="260" height="48" rx="0 0 0 8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="20" y="29" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#1E293B">Domaine cible</text>

    <rect x="270" y="0" width="300" height="48" rx="0 0 0 0" fill="#FAF5FF" stroke="#E9D5FF"/>
    <text x="420" y="29" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#6B21A8" text-anchor="middle">Manufacturier, Machines, Robotique</text>

    <rect x="580" y="0" width="300" height="48" rx="0 0 8 0" fill="#F0F9FF" stroke="#BAE6FD"/>
    <text x="730" y="29" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#0369A1" text-anchor="middle">Procédés continus, Pétrochimie (ATEX)</text>
  </g>
</svg>'''

def get_svg_signaux():
    return '''<svg viewBox="0 0 920 380" class="academic-svg" aria-label="Signaux électriques RS-485 versus MBP">
  <!-- Left Side: RS-485 Differential Voltage -->
  <g transform="translate(15, 10)">
    <rect x="0" y="0" width="430" height="355" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="0" y="0" width="430" height="40" rx="10 10 0 0" fill="#1F3A5F"/>
    <text x="215" y="26" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">RS-485 : DIFFÉRENTIEL DE TENSION</text>

    <!-- Axes -->
    <line x1="45" y1="60" x2="45" y2="280" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="45" y1="170" x2="400" y2="170" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="35" y="100" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" fill="#64748B" text-anchor="end">+3.5 V</text>
    <text x="35" y="174" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" fill="#64748B" text-anchor="end">0 V</text>
    <text x="35" y="240" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" fill="#64748B" text-anchor="end">-3.5 V</text>

    <!-- Bit markers -->
    <text x="90" y="80" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#1E293B">Bit '1'</text>
    <text x="180" y="80" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#1E293B">Bit '0'</text>
    <text x="270" y="80" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#1E293B">Bit '1'</text>
    <text x="350" y="80" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#1E293B">Bit '0'</text>

    <!-- Signal Wire B (Red) -->
    <path d="M 45 110 L 130 110 L 140 230 L 220 230 L 230 110 L 310 110 L 320 230 L 390 230" stroke="#DC2626" stroke-width="3" fill="none"/>
    <text x="402" y="115" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#DC2626">Fil B (+)</text>

    <!-- Signal Wire A (Green) in anti-phase -->
    <path d="M 45 230 L 130 230 L 140 110 L 220 110 L 230 230 L 310 230 L 320 110 L 390 110" stroke="#16A34A" stroke-width="3" fill="none"/>
    <text x="402" y="235" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#16A34A">Fil A (-)</text>

    <!-- Formula -->
    <rect x="25" y="295" width="380" height="45" rx="6" fill="#F1F5F9"/>
    <text x="215" y="315" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">V_diff = (V_B - V_A) : &gt; +0.2V ➔ '1' | &lt; -0.2V ➔ '0'</text>
    <text x="215" y="332" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Les parasites en mode commun s'annulent par soustraction</text>
  </g>

  <!-- Right Side: MBP Manchester Bus Powered -->
  <g transform="translate(470, 10)">
    <rect x="0" y="0" width="435" height="355" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="0" y="0" width="435" height="40" rx="10 10 0 0" fill="#0284C7"/>
    <text x="217" y="26" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">MBP : MODULATION DE COURANT ±9 mA</text>

    <!-- DC Voltage line -->
    <line x1="45" y1="75" x2="390" y2="75" stroke="#EAB308" stroke-width="3"/>
    <text x="400" y="80" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#CA8A04">U_dc ≈ 24 V</text>
    <text x="50" y="68" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#854D0E">Alimentation continue permanente du capteur</text>

    <!-- Manchester Current Waveform -->
    <line x1="45" y1="130" x2="45" y2="280" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="45" y1="200" x2="390" y2="200" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="35" y="165" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" fill="#64748B" text-anchor="end">+9 mA</text>
    <text x="35" y="204" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" fill="#64748B" text-anchor="end">I_base</text>
    <text x="35" y="245" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" fill="#64748B" text-anchor="end">-9 mA</text>

    <!-- Bit cells -->
    <text x="100" y="145" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#0284C7">Bit '0' (Montant)</text>
    <text x="210" y="145" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#0284C7">Bit '1' (Descendant)</text>
    <text x="320" y="145" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#0284C7">Bit '0' (Montant)</text>

    <!-- Manchester pulses -->
    <!-- Bit 0: Low then High -->
    <path d="M 45 240 L 95 240 L 95 160 L 150 160" stroke="#0284C7" stroke-width="3" fill="none"/>
    <!-- Bit 1: High then Low -->
    <path d="M 150 160 L 205 160 L 205 240 L 260 240" stroke="#0284C7" stroke-width="3" fill="none"/>
    <!-- Bit 0: Low then High -->
    <path d="M 260 240 L 315 240 L 315 160 L 370 160" stroke="#0284C7" stroke-width="3" fill="none"/>

    <!-- Formula -->
    <rect x="25" y="295" width="385" height="45" rx="6" fill="#F0F9FF"/>
    <text x="217" y="315" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#0369A1" text-anchor="middle">Débit fixe 31,25 kbit/s · Codage Manchester</text>
    <text x="217" y="332" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#0284C7" text-anchor="middle">Données + Alimentation sur les 2 seuls mêmes fils (ATEX / FISCO)</text>
  </g>
</svg>'''

def get_svg_db9():
    return '''<svg viewBox="0 0 920 380" class="academic-svg" aria-label="Connecteur DB9 PROFIBUS DP et terminaison active">
  <defs>
    <filter id="shadowDb9" x="-3%" y="-3%" width="106%" height="106%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Left: DB9 Connector Representation -->
  <g transform="translate(25, 20)" filter="url(#shadowDb9)">
    <path d="M 30,10 L 270,10 L 250,280 L 50,280 Z" fill="#E2E8F0" stroke="#475569" stroke-width="3"/>
    <path d="M 50,30 L 250,30 L 235,260 L 65,260 Z" fill="#1E293B" stroke="#0F172A" stroke-width="2"/>
    <text x="150" y="60" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#F8FAFC" text-anchor="middle">CONNECTEUR SUB-D 9</text>

    <!-- Top Row Pins 1 to 5 -->
    <!-- Pin 1 -->
    <circle cx="85" cy="100" r="12" fill="#94A3B8" stroke="#FFFFFF" stroke-width="2"/>
    <text x="85" y="104" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#0F172A" text-anchor="middle">1</text>
    <!-- Pin 2 -->
    <circle cx="118" cy="100" r="12" fill="#64748B" stroke="#FFFFFF" stroke-width="2"/>
    <text x="118" y="104" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2</text>
    <!-- Pin 3: Data B (Red) -->
    <circle cx="150" cy="100" r="15" fill="#DC2626" stroke="#FFFFFF" stroke-width="3"/>
    <text x="150" y="105" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3</text>
    <!-- Pin 4: RTS -->
    <circle cx="182" cy="100" r="12" fill="#64748B" stroke="#FFFFFF" stroke-width="2"/>
    <text x="182" y="104" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4</text>
    <!-- Pin 5: DGND (0V) -->
    <circle cx="215" cy="100" r="15" fill="#0284C7" stroke="#FFFFFF" stroke-width="3"/>
    <text x="215" y="105" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">5</text>

    <!-- Bottom Row Pins 6 to 9 -->
    <!-- Pin 6: VP (+5V) -->
    <circle cx="100" cy="160" r="15" fill="#D97706" stroke="#FFFFFF" stroke-width="3"/>
    <text x="100" y="165" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">6</text>
    <!-- Pin 7 -->
    <circle cx="134" cy="160" r="12" fill="#64748B" stroke="#FFFFFF" stroke-width="2"/>
    <text x="134" y="164" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">7</text>
    <!-- Pin 8: Data A (Green) -->
    <circle cx="168" cy="160" r="15" fill="#16A34A" stroke="#FFFFFF" stroke-width="3"/>
    <text x="168" y="165" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">8</text>
    <!-- Pin 9 -->
    <circle cx="200" cy="160" r="12" fill="#64748B" stroke="#FFFFFF" stroke-width="2"/>
    <text x="200" y="164" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">9</text>

    <!-- Callouts below connector -->
    <text x="150" y="210" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#DC2626" text-anchor="middle">Broche 3 : Signal B (Rouge)</text>
    <text x="150" y="230" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#16A34A" text-anchor="middle">Broche 8 : Signal A (Vert)</text>
    <text x="150" y="250" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#E2E8F0" text-anchor="middle">Broche 6: +5V VP · Broche 5: 0V DGND</text>
  </g>

  <!-- Right: Active Termination Circuit Schematic -->
  <g transform="translate(340, 20)">
    <rect x="0" y="0" width="555" height="340" rx="10" fill="#FAF5FF" stroke="#C084FC" stroke-width="2"/>
    <rect x="0" y="0" width="555" height="38" rx="10 10 0 0" fill="#7E22CE"/>
    <text x="277" y="25" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">CIRCUIT DE TERMINAISON ACTIVE DE BUS</text>

    <!-- VP line (+5V) -->
    <line x1="50" y1="70" x2="500" y2="70" stroke="#D97706" stroke-width="3"/>
    <text x="45" y="65" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#D97706">Broche 6 (+5V VP)</text>

    <!-- Resistor 390 Ohm Pull-up -->
    <line x1="200" y1="70" x2="200" y2="100" stroke="#475569" stroke-width="2"/>
    <rect x="185" y="100" width="30" height="45" fill="#FFFFFF" stroke="#1E293B" stroke-width="2"/>
    <text x="200" y="127" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#1E293B" text-anchor="middle">390 Ω</text>
    <line x1="200" y1="145" x2="200" y2="170" stroke="#475569" stroke-width="2"/>

    <!-- Data Line B (Pin 3) -->
    <line x1="50" y1="170" x2="500" y2="170" stroke="#DC2626" stroke-width="3"/>
    <text x="45" y="165" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#DC2626">Broche 3 : Data B (Rouge)</text>

    <!-- Middle Resistor 220 Ohm -->
    <line x1="280" y1="170" x2="280" y2="185" stroke="#475569" stroke-width="2"/>
    <rect x="265" y="185" width="30" height="45" fill="#FFFFFF" stroke="#7E22CE" stroke-width="2.5"/>
    <text x="280" y="212" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#7E22CE" text-anchor="middle">220 Ω</text>
    <line x1="280" y1="230" x2="280" y2="245" stroke="#475569" stroke-width="2"/>

    <!-- Data Line A (Pin 8) -->
    <line x1="50" y1="245" x2="500" y2="245" stroke="#16A34A" stroke-width="3"/>
    <text x="45" y="240" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#16A34A">Broche 8 : Data A (Vert)</text>

    <!-- Resistor 390 Ohm Pull-down -->
    <line x1="360" y1="245" x2="360" y2="265" stroke="#475569" stroke-width="2"/>
    <rect x="345" y="265" width="30" height="40" fill="#FFFFFF" stroke="#1E293B" stroke-width="2"/>
    <text x="360" y="290" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#1E293B" text-anchor="middle">390 Ω</text>
    <line x1="360" y1="305" x2="360" y2="320" stroke="#475569" stroke-width="2"/>

    <!-- DGND line (0V) -->
    <line x1="50" y1="320" x2="500" y2="320" stroke="#0284C7" stroke-width="3"/>
    <text x="45" y="315" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#0284C7">Broche 5 : DGND (0V)</text>

    <!-- Switch S1 indicator -->
    <g transform="translate(420, 110)">
      <rect x="0" y="0" width="95" height="110" rx="6" fill="#FFFFFF" stroke="#DC2626" stroke-width="2"/>
      <text x="47" y="22" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#DC2626" text-anchor="middle">COMMUTATEUR</text>
      <rect x="15" y="32" width="65" height="28" rx="4" fill="#DC2626"/>
      <text x="47" y="51" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">ON</text>
      <text x="47" y="80" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Extrémités</text>
      <text x="47" y="98" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#16A34A" text-anchor="middle">(OFF au milieu)</text>
    </g>
  </g>
</svg>'''

def get_svg_chaine_liaison():
    return '''<svg viewBox="0 0 940 370" class="academic-svg" aria-label="Chaîne de liaison automate vers PROFIBUS DP, coupleur et transmetteurs PA">
  <defs>
    <marker id="arrowRight" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#1F3A5F"/>
    </marker>
  </defs>

  <!-- 1. Automate PLC -->
  <g transform="translate(20, 60)">
    <rect x="0" y="0" width="150" height="230" rx="8" fill="#1F3A5F" stroke="#0F172A" stroke-width="2"/>
    <rect x="10" y="15" width="130" height="40" rx="4" fill="#334155"/>
    <text x="75" y="40" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8" text-anchor="middle">SIEMENS S7</text>
    <text x="75" y="90" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">AUTOMATE</text>
    <text x="75" y="112" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" fill="#94A3B8" text-anchor="middle">Maître DP (Classe 1)</text>
    <!-- DB9 port -->
    <rect x="40" y="160" width="70" height="30" rx="4" fill="#64748B" stroke="#CBD5E1"/>
    <text x="75" y="180" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Port DP</text>
  </g>

  <!-- Cable DP (Violet) -->
  <g transform="translate(170, 175)">
    <line x1="0" y1="0" x2="130" y2="0" stroke="#7E22CE" stroke-width="8" stroke-linecap="round"/>
    <text x="65" y="-12" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#7E22CE" text-anchor="middle">PROFIBUS DP</text>
    <text x="65" y="22" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#6B21A8" text-anchor="middle">RS-485 · 1,5 Mbit/s</text>
  </g>

  <!-- 2. Coupleur DP/PA -->
  <g transform="translate(300, 45)">
    <rect x="0" y="0" width="170" height="260" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="2.5"/>
    <rect x="0" y="0" width="170" height="40" rx="8 8 0 0" fill="#0284C7"/>
    <text x="85" y="26" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#FFFFFF" text-anchor="middle">COUPLEUR DP / PA</text>
    
    <text x="85" y="75" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">Passerelle physique</text>
    <text x="85" y="95" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#475569" text-anchor="middle">1. Adaptation débit :</text>
    <text x="85" y="112" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#7E22CE" text-anchor="middle">1.5 Mbit/s ➔ 31.25 kbit/s</text>

    <text x="85" y="145" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#475569" text-anchor="middle">2. Conversion signal :</text>
    <text x="85" y="162" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#0284C7" text-anchor="middle">RS-485 ➔ MBP (Courant)</text>

    <text x="85" y="195" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#475569" text-anchor="middle">3. Télé-alimentation :</text>
    <rect x="25" y="210" width="120" height="28" rx="4" fill="#FEF3C7" stroke="#F59E0B"/>
    <text x="85" y="229" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#B45309" text-anchor="middle">Injecteur 24 V DC</text>
  </g>

  <!-- Cable PA (Blue) Trunk -->
  <g transform="translate(470, 175)">
    <line x1="0" y1="0" x2="120" y2="0" stroke="#0284C7" stroke-width="8" stroke-linecap="round"/>
    <text x="60" y="-12" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#0284C7" text-anchor="middle">TRUNK PA (Bleu)</text>
    <text x="60" y="22" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#0369A1" text-anchor="middle">MBP · 31,25 kbit/s</text>
  </g>

  <!-- 3. Boîte de dérivation (Junction Box) -->
  <g transform="translate(590, 85)">
    <rect x="0" y="0" width="120" height="180" rx="8" fill="#14532D" stroke="#22C55E" stroke-width="2"/>
    <text x="60" y="30" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">BOÎTE DE</text>
    <text x="60" y="48" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">DÉRIVATION</text>
    <text x="60" y="70" font-family="'Segoe UI', Calibri, sans-serif" font-size="10" fill="#86EFAC" text-anchor="middle">FieldConnex IP67</text>
    <!-- Spurs outputs -->
    <circle cx="110" cy="95" r="5" fill="#38BDF8"/>
    <circle cx="110" cy="135" r="5" fill="#38BDF8"/>
    <circle cx="110" cy="175" r="5" fill="#38BDF8"/>
  </g>

  <!-- Spurs & Field Transmitters -->
  <!-- Spur 1: Pression -->
  <path d="M 700 95 L 750 95" stroke="#0284C7" stroke-width="4"/>
  <g transform="translate(750, 75)">
    <rect x="0" y="0" width="165" height="42" rx="6" fill="#F0F9FF" stroke="#0284C7" stroke-width="1.5"/>
    <text x="82" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#0369A1" text-anchor="middle">Transmetteur Pression</text>
    <text x="82" y="34" font-family="'Segoe UI', Calibri, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">SITRANS P / Rosemount</text>
  </g>

  <!-- Spur 2: Température -->
  <path d="M 700 135 L 750 135" stroke="#0284C7" stroke-width="4"/>
  <g transform="translate(750, 120)">
    <rect x="0" y="0" width="165" height="42" rx="6" fill="#F0F9FF" stroke="#0284C7" stroke-width="1.5"/>
    <text x="82" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#0369A1" text-anchor="middle">Sonde Température</text>
    <text x="82" y="34" font-family="'Segoe UI', Calibri, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">PT100 / Thermocouple</text>
  </g>

  <!-- Spur 3: Débit / Vanne -->
  <path d="M 700 175 L 750 175" stroke="#0284C7" stroke-width="4"/>
  <g transform="translate(750, 165)">
    <rect x="0" y="0" width="165" height="42" rx="6" fill="#F0F9FF" stroke="#0284C7" stroke-width="1.5"/>
    <text x="82" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#0369A1" text-anchor="middle">Positionneur Vanne</text>
    <text x="82" y="34" font-family="'Segoe UI', Calibri, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Fisher / Zone ATEX</text>
  </g>

  <!-- Bottom Global Summary Banner -->
  <rect x="20" y="315" width="900" height="42" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="470" y="341" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#1F3A5F" text-anchor="middle">
    Totalement transparent pour le programme automate : les instruments PA apparaissent comme des esclaves DP normaux !
  </text>
</svg>'''

def get_svg_pile_profinet():
    return '''<svg viewBox="0 0 920 380" class="academic-svg" aria-label="Pile protocolaire PROFINET et triptyque d'adressage MAC IP Nom">
  <!-- Left Side: Stack comparison -->
  <g transform="translate(15, 10)">
    <rect x="0" y="0" width="440" height="355" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="0" y="0" width="440" height="40" rx="10 10 0 0" fill="#1F3A5F"/>
    <text x="220" y="26" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">COHABITATION DES PILES PROTOCOLAIRES</text>

    <!-- App Layer -->
    <rect x="30" y="60" width="380" height="45" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
    <text x="220" y="87" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Application Industrielle / Données Process &amp; IHM</text>

    <!-- Branching -->
    <!-- Left Branch: TCP/IP (Standard) -->
    <g transform="translate(30, 120)">
      <rect x="0" y="0" width="180" height="90" rx="6" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="90" y="24" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">Pile TCP / UDP</text>
      <text x="90" y="44" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">Protocole IP (Couche 3)</text>
      <rect x="15" y="55" width="150" height="24" rx="4" fill="#E2E8F0"/>
      <text x="90" y="72" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#475569" text-anchor="middle">PROFINET NRT (10-100 ms)</text>
    </g>

    <!-- Right Branch: PROFINET RT (Bypass) -->
    <g transform="translate(230, 120)">
      <rect x="0" y="0" width="180" height="90" rx="6" fill="#DCFCE7" stroke="#22C55E" stroke-width="2"/>
      <text x="90" y="28" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#15803D" text-anchor="middle">PROFINET RT</text>
      <text x="90" y="50" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#166534" text-anchor="middle">EtherType 0x8892</text>
      <rect x="15" y="58" width="150" height="24" rx="4" fill="#BBF7D0"/>
      <text x="90" y="75" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#14532D" text-anchor="middle">Bypass IP : &lt; 1 ms (Temps réel)</text>
    </g>

    <!-- Ethernet Layer 2 -->
    <rect x="30" y="225" width="380" height="45" rx="6" fill="#1F3A5F"/>
    <text x="220" y="252" font-family="'Segoe UI', Calibri, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Couche 2 : TRAME ETHERNET (IEEE 802.3)</text>

    <!-- Physical Layer 1 -->
    <rect x="30" y="280" width="380" height="40" rx="6" fill="#0F172A"/>
    <text x="220" y="305" font-family="'Segoe UI', Calibri, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8" text-anchor="middle">Couche 1 : CÂBLE VERT 100BASE-TX / FIBRE</text>
  </g>

  <!-- Right Side: The 3 Identifiers -->
  <g transform="translate(470, 10)">
    <rect x="0" y="0" width="435" height="355" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="0" y="0" width="435" height="40" rx="10 10 0 0" fill="#15803D"/>
    <text x="217" y="26" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">LE TRIPTYQUE D'ADRESSAGE PROFINET</text>

    <!-- 1. Device Name -->
    <g transform="translate(20, 55)">
      <rect x="0" y="0" width="395" height="85" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
      <text x="15" y="26" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#166534">1. Nom d'appareil (Device Name)</text>
      <rect x="15" y="35" width="220" height="24" rx="4" fill="#DCFCE7"/>
      <text x="25" y="52" font-family="Consolas, monospace" font-size="13" font-weight="bold" fill="#14532D">station-et200-cuve1</text>
      <text x="15" y="75" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#15803D">Défini dans le projet TIA Portal par l'automaticien (clé primaire)</text>
    </g>

    <!-- 2. MAC Address -->
    <g transform="translate(20, 150)">
      <rect x="0" y="0" width="395" height="85" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="15" y="26" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#1E293B">2. Adresse MAC (Physique - Couche 2)</text>
      <rect x="15" y="35" width="220" height="24" rx="4" fill="#E2E8F0"/>
      <text x="25" y="52" font-family="Consolas, monospace" font-size="13" font-weight="bold" fill="#0F172A">00:1B:1B:34:C2:A1</text>
      <text x="15" y="75" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#475569">Gravée en usine. Découverte via le protocole DCP sur le réseau local</text>
    </g>

    <!-- 3. IP Address -->
    <g transform="translate(20, 245)">
      <rect x="0" y="0" width="395" height="95" rx="6" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.5"/>
      <text x="15" y="26" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#1E40AF">3. Adresse IP (Logique - Couche 3)</text>
      <rect x="15" y="35" width="220" height="24" rx="4" fill="#DBEAFE"/>
      <text x="25" y="52" font-family="Consolas, monospace" font-size="13" font-weight="bold" fill="#1E3A8A">192.168.0.10</text>
      <text x="15" y="75" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#1D4ED8">Attribuée automatiquement par le contrôleur au démarrage via le nom !</text>
      <text x="15" y="88" font-family="'Segoe UI', Calibri, sans-serif" font-size="10" font-weight="bold" fill="#B45309">Remplacement sans console de programmation</text>
    </g>
  </g>
</svg>'''

def get_svg_architecture_complete():
    return '''<svg viewBox="0 0 940 450" class="academic-svg" aria-label="Architecture industrielle complète du capteur au SCADA et ERP">
  <defs>
    <filter id="shadowArch" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-opacity="0.1"/>
    </filter>
  </defs>

  <!-- Level 4: ERP / Entreprise -->
  <g transform="translate(20, 15)" filter="url(#shadowArch)">
    <rect x="0" y="0" width="900" height="60" rx="8" fill="#0F172A"/>
    <text x="30" y="35" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#38BDF8">NIVEAU 4 · GESTION DE L'ENTREPRISE (ERP / CLOUD)</text>
    <text x="30" y="50" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#94A3B8">Planification de la production, logistique, commandes clients, maintenance globale</text>
    <rect x="730" y="15" width="150" height="30" rx="5" fill="#1E293B" stroke="#38BDF8"/>
    <text x="805" y="35" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Serveurs SAP / ERP</text>
  </g>

  <!-- Firewall / DMZ Bar -->
  <g transform="translate(20, 80)">
    <line x1="0" y1="12" x2="900" y2="12" stroke="#DC2626" stroke-width="2" stroke-dasharray="6,4"/>
    <rect x="360" y="0" width="180" height="24" rx="4" fill="#DC2626"/>
    <text x="450" y="16" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">🔒 PARE-FEU INDUSTRIEL / DMZ</text>
  </g>

  <!-- Level 3: Usine / Supervision MES & SCADA -->
  <g transform="translate(20, 110)" filter="url(#shadowArch)">
    <rect x="0" y="0" width="900" height="70" rx="8" fill="#1F3A5F"/>
    <text x="30" y="30" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#E2E8F0">NIVEAU 3 · SUPERVISION D'USINE (MES / SCADA)</text>
    <text x="30" y="48" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" fill="#94A3B8">Réseau Ethernet industriel TCP/IP · Conduite d'atelier · Historisation &amp; Suivi qualité</text>
    
    <g transform="translate(560, 15)">
      <rect x="0" y="0" width="150" height="40" rx="4" fill="#334155" stroke="#CBD5E1"/>
      <text x="75" y="24" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Postes SCADA</text>
    </g>
    <g transform="translate(730, 15)">
      <rect x="0" y="0" width="150" height="40" rx="4" fill="#334155" stroke="#CBD5E1"/>
      <text x="75" y="24" font-family="'Segoe UI', Calibri, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Serveur MES / BDD</text>
    </g>
  </g>

  <!-- Level 2: Contrôle Commande / PROFINET -->
  <g transform="translate(20, 190)" filter="url(#shadowArch)">
    <rect x="0" y="0" width="900" height="85" rx="8" fill="#F0FDF4" stroke="#22C55E" stroke-width="2"/>
    <text x="30" y="28" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#15803D">NIVEAU 2 · CELLULE &amp; COMMANDE (PROFINET RT / IRT)</text>
    <line x1="30" y1="42" x2="870" y2="42" stroke="#16A34A" stroke-width="4"/>
    <text x="450" y="38" font-family="'Segoe UI', Calibri, sans-serif" font-size="10" font-weight="bold" fill="#166534" text-anchor="middle">Anneau redondant PROFINET (Câbles verts) · Switchs industriels SCALANCE</text>

    <!-- Equipment boxes -->
    <g transform="translate(50, 48)">
      <rect x="0" y="0" width="140" height="30" rx="4" fill="#1F3A5F"/>
      <text x="70" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">PLC Siemens S7-1500</text>
    </g>
    <g transform="translate(220, 48)">
      <rect x="0" y="0" width="140" height="30" rx="4" fill="#0284C7"/>
      <text x="70" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Pupitre IHM (Touch)</text>
    </g>
    <g transform="translate(390, 48)">
      <rect x="0" y="0" width="140" height="30" rx="4" fill="#7E22CE"/>
      <text x="70" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Îlot Variateurs Sinamics</text>
    </g>
    <g transform="translate(560, 48)">
      <rect x="0" y="0" width="140" height="30" rx="4" fill="#D97706"/>
      <text x="70" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Robot Industriel</text>
    </g>
    <g transform="translate(730, 48)">
      <rect x="0" y="0" width="140" height="30" rx="4" fill="#059669"/>
      <text x="70" y="20" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Coupleur DP / PA</text>
    </g>
  </g>

  <!-- Level 1: Périphérie déportée & Bus PROFIBUS DP -->
  <g transform="translate(20, 285)" filter="url(#shadowArch)">
    <rect x="0" y="0" width="900" height="75" rx="8" fill="#FAF5FF" stroke="#A855F7" stroke-width="2"/>
    <text x="30" y="25" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#7E22CE">NIVEAU 1 · PÉRIPHÉRIE DÉPORTÉE (PROFIBUS DP · RS-485)</text>
    <line x1="30" y1="36" x2="870" y2="36" stroke="#9333EA" stroke-width="4"/>

    <g transform="translate(60, 42)">
      <rect x="0" y="0" width="170" height="26" rx="4" fill="#7E22CE"/>
      <text x="85" y="18" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">E/S Déportées ET 200S</text>
    </g>
    <g transform="translate(270, 42)">
      <rect x="0" y="0" width="170" height="26" rx="4" fill="#7E22CE"/>
      <text x="85" y="18" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Démarreurs Moteurs</text>
    </g>
    <g transform="translate(480, 42)">
      <rect x="0" y="0" width="170" height="26" rx="4" fill="#7E22CE"/>
      <text x="85" y="18" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Vanne Multipôle AS-i</text>
    </g>
    <g transform="translate(690, 42)">
      <rect x="0" y="0" width="170" height="26" rx="4" fill="#0284C7"/>
      <text x="85" y="18" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Liaison Tronc PA (MBP)</text>
    </g>
  </g>

  <!-- Level 0: Instrumentation de terrain & Zone ATEX -->
  <g transform="translate(20, 370)" filter="url(#shadowArch)">
    <rect x="0" y="0" width="900" height="70" rx="8" fill="#F0F9FF" stroke="#0284C7" stroke-width="2"/>
    <text x="30" y="24" font-family="Georgia, serif" font-size="14" font-weight="bold" fill="#0369A1">NIVEAU 0 · PROCÉDÉ PHYSIQUE &amp; INSTRUMENTATION (PROFIBUS PA / 4–20 mA)</text>
    
    <g transform="translate(50, 33)">
      <rect x="0" y="0" width="180" height="28" rx="4" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
      <text x="90" y="19" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#0369A1" text-anchor="middle">Transmetteur Pression (PA)</text>
    </g>
    <g transform="translate(260, 33)">
      <rect x="0" y="0" width="180" height="28" rx="4" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
      <text x="90" y="19" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#0369A1" text-anchor="middle">Débitmètre Magnétique (PA)</text>
    </g>
    <g transform="translate(470, 33)">
      <rect x="0" y="0" width="180" height="28" rx="4" fill="#FFFFFF" stroke="#334155" stroke-width="1.5"/>
      <text x="90" y="19" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">Boucle de courant 4–20 mA</text>
    </g>
    <g transform="translate(680, 33)">
      <rect x="0" y="0" width="180" height="28" rx="4" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5"/>
      <text x="90" y="19" font-family="'Segoe UI', Calibri, sans-serif" font-size="11" font-weight="bold" fill="#B45309" text-anchor="middle">Zone Ex / Sécurité Intrinsèque</text>
    </g>
  </g>
</svg>'''

print("SVG definitions ready.")
