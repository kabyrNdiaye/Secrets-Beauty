import os

# HTML Content of the new menu structure - UPDATED: CORRECT COLORS #5C5045
new_menu_html = """                    <!-- Audace Style Mobile Menu -->
                    <div id="mobile-menu"
                        class="fixed inset-0 z-[1000] invisible md:hidden h-screen w-screen">
                        
                        <!-- Backdrop -->
                        <div id="menu-backdrop" class="absolute inset-0 bg-black/50 opacity-0 transition-opacity duration-300" onclick="toggleMenu()"></div>
                        
                        <!-- Menu Panel -->
                        <div id="menu-panel" class="absolute inset-y-0 left-0 w-[85%] max-w-sm h-full bg-white shadow-2xl transform -translate-x-full transition-transform duration-300 flex flex-col">
                            
                            <!-- Header: Logo & Close -->
                            <div class="px-6 py-4 flex justify-between items-center bg-white z-20">
                                <button id="close-menu-btn" class="text-black">
                                    <i data-lucide="x" class="w-6 h-6"></i>
                                </button>
                                <img src="../assets/images/logo-icon.png" alt="Logo" class="h-10 w-auto object-contain">
                                <div class="w-6"></div> <!-- Spacer for balance -->
                            </div>

                            <!-- Search Bar -->
                            <div class="px-6 py-4 border-b border-gray-100">
                                <div class="relative">
                                    <input type="text" placeholder="Les produits de recherche ici..." 
                                        class="w-full h-10 px-4 pr-10 bg-white border border-gray-200 text-sm focus:outline-none focus:border-[#C5A059] placeholder-gray-400">
                                    <button class="absolute right-0 top-0 h-10 w-10 flex items-center justify-center bg-[#C5A059] text-white">
                                        <i data-lucide="search" class="w-4 h-4"></i>
                                    </button>
                                </div>
                            </div>

                            <!-- Slider Container -->
                            <div class="flex-1 relative overflow-hidden">
                                <div id="menu-slider" class="absolute inset-0 w-[200%] flex transition-transform duration-300">
                                    
                                    <!-- Main Menu List -->
                                    <div class="w-1/2 h-full overflow-y-auto bg-white">
                                        <nav class="flex flex-col">
                                            <a href="../index.html" class="flex items-center px-6 py-4 border-b border-gray-100 border-l-4 border-l-[#C5A059] text-sm font-bold text-[#5C5045] uppercase tracking-wide bg-gray-50">
                                                Accueil
                                            </a>
                                            <button id="open-services-btn" class="flex items-center justify-between px-6 py-4 border-b border-gray-100 border-l-4 border-l-transparent text-sm font-bold text-[#5C5045] uppercase tracking-wide hover:bg-gray-50 w-full">
                                                <span>Nos Services</span>
                                                <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400"></i>
                                            </button>
                                            <a href="../reservation.html" class="flex items-center px-6 py-4 border-b border-gray-100 border-l-4 border-l-transparent text-sm font-bold text-[#5C5045] uppercase tracking-wide hover:bg-gray-50">
                                                Réservation
                                            </a>
                                            <a href="../contact.html" class="flex items-center px-6 py-4 border-b border-gray-100 border-l-4 border-l-transparent text-sm font-bold text-[#5C5045] uppercase tracking-wide hover:bg-gray-50">
                                                Contact
                                            </a>
                                        </nav>
                                    </div>

                                    <!-- Submenu List (Services) -->
                                    <div class="w-1/2 h-full overflow-y-auto bg-white">
                                        <button id="back-to-main-btn" class="flex items-center gap-2 px-6 py-5 text-sm font-bold text-[#5C5045] uppercase tracking-wide w-full hover:bg-gray-50">
                                            <i data-lucide="chevron-left" class="w-4 h-4"></i>
                                            <span>Back</span>
                                        </button>
                                        <nav class="flex flex-col border-t border-gray-100">
                                            <a href="laser.html" class="flex items-center px-6 py-4 border-b border-gray-100 text-sm font-bold text-[#5C5045] uppercase tracking-wide hover:bg-gray-50">
                                                Épilation Laser
                                            </a>
                                            <a href="onglerie.html" class="flex items-center px-6 py-4 border-b border-gray-100 text-sm font-bold text-[#5C5045] uppercase tracking-wide hover:bg-gray-50">
                                                Onglerie
                                            </a>
                                            <a href="regard.html" class="flex items-center px-6 py-4 border-b border-gray-100 text-sm font-bold text-[#5C5045] uppercase tracking-wide hover:bg-gray-50">
                                                Regard
                                            </a>
                                            <a href="visage.html" class="flex items-center px-6 py-4 border-b border-gray-100 text-sm font-bold text-[#5C5045] uppercase tracking-wide hover:bg-gray-50">
                                                Visage
                                            </a>
                                            <a href="massages.html" class="flex items-center px-6 py-4 border-b border-gray-100 text-sm font-bold text-[#5C5045] uppercase tracking-wide hover:bg-gray-50">
                                                Massages
                                            </a>
                                            <a href="forfaits.html" class="flex items-center px-6 py-4 border-b border-gray-100 text-sm font-bold text-[#5C5045] uppercase tracking-wide hover:bg-gray-50">
                                                Forfaits
                                            </a>
                                        </nav>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>"""

# Files to update
root_files = ['contact.html', 'reservation.html', 'gallery.html', 'services.html']
service_files = [
    'services/laser.html', 'services/onglerie.html', 'services/regard.html',
    'services/visage.html', 'services/massages.html', 'services/forfaits.html',
    'services/epilation-wax.html'
]

def get_menu_html(is_root):
    if is_root:
        return new_menu_html.replace('../assets', 'assets').replace('../index', 'index').replace('../contact', 'contact').replace('../reservation', 'reservation').replace('href="laser.html"', 'href="services/laser.html"').replace('href="onglerie.html"', 'href="services/onglerie.html"').replace('href="regard.html"', 'href="services/regard.html"').replace('href="visage.html"', 'href="services/visage.html"').replace('href="massages.html"', 'href="services/massages.html"').replace('href="forfaits.html"', 'href="services/forfaits.html"')
    else:
        return new_menu_html

def update_file(fname, is_root):
    if not os.path.exists(fname): return

    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = '<!-- Audace Style Mobile Menu -->'
    
    # Locate start
    s_idx = content.find(start_marker)
    if s_idx == -1:
        print(f"Marker not found in {fname}")
        return
            
    # Locate end using stack logic from known block start
    div_start = content.find('<div id="mobile-menu"', s_idx)
    idx = div_start
    stack = 0
    end_idx = -1
    
    while idx < len(content):
        if content.startswith('<div', idx):
            stack += 1
            idx += 4
        elif content.startswith('</div', idx):
            stack -= 1
            idx += 5
            if stack == 0:
                end_idx = idx
                break
        else:
            idx += 1
            
    if end_idx != -1:
        menu_replacement = get_menu_html(is_root)
        content = content[:s_idx] + menu_replacement + content[end_idx:]
        print(f"Updated HTML in {fname}")

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

for f in root_files:
    update_file(f, True)

for f in service_files:
    update_file(f, False)
