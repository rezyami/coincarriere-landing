with open('index.html', 'r') as f:
    content = f.read()

start_marker = '    <!-- Process Section -->'
end_marker = '    <!-- Technical Tests Showcase Section -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

new_section = """    <!-- Process Section -->
    <section class="bg-[#f8fafc] py-24 px-5 relative overflow-hidden z-0">
        <!-- Network Background Pattern -->
        <div class="absolute inset-0 opacity-40 pointer-events-none" style="background-image: radial-gradient(#0077b6 1px, transparent 1px); background-size: 30px 30px;"></div>
        
        <div class="max-w-[1200px] mx-auto relative z-10">
            <div class="text-center mb-24">
                <h2 class="text-3xl md:text-[2.5rem] font-extrabold text-primary inline-block relative bg-white px-6 py-2 rounded-full shadow-sm">
                    Un processus <span class="relative">simple et efficace
                        <svg class="absolute w-full h-3 -bottom-1 left-0 text-accent" viewBox="0 0 100 10" preserveAspectRatio="none">
                            <path d="M0 8 Q 50 2 100 8" stroke="currentColor" stroke-width="4" fill="none" stroke-linecap="round"/>
                        </svg>
                    </span>
                </h2>
            </div>

            <div class="relative mt-16">
                <!-- Connecting dotted line -->
                <div class="hidden lg:block absolute top-[48px] left-[12%] right-[12%] border-t-[3px] border-dotted border-[#b4dc02] opacity-60 -z-10">
                    <!-- Dots on the line -->
                    <div class="absolute -top-[5.5px] left-0 w-2 h-2 bg-accent rounded-full"></div>
                    <div class="absolute -top-[5.5px] left-[33%] w-2 h-2 bg-accent rounded-full"></div>
                    <div class="absolute -top-[5.5px] left-[66%] w-2 h-2 bg-accent rounded-full"></div>
                    <div class="absolute -top-[5.5px] right-0 w-2 h-2 bg-accent rounded-full"></div>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-6">
                    
                    <!-- Card 1 -->
                    <div class="relative bg-white rounded-2xl border-2 border-accent p-8 pt-16 text-center shadow-[0_10px_30px_rgba(0,119,182,0.08)] hover:-translate-y-2 hover:shadow-[0_15px_40px_rgba(0,119,182,0.15)] transition-all duration-300 fade-in">
                        <!-- Number Badge -->
                        <div class="absolute top-0 left-0 bg-accent text-white font-extrabold text-xl w-12 h-12 flex items-center justify-center rounded-br-2xl rounded-tl-xl shadow-sm">1</div>
                        
                        <!-- Icon -->
                        <div class="absolute -top-12 left-1/2 -translate-x-1/2 w-24 h-24 bg-[#eef5fa] rounded-full border-[6px] border-primary flex items-center justify-center shadow-lg">
                            <svg class="w-10 h-10 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M10.34 15.84c-.688-.06-1.386-.09-2.09-.09H7a4 4 0 110-8h.5c.704 0 1.402-.03 2.09-.09m0 8.18c-1.365.12-2.753.18-4.15.18H4.5A2.5 2.5 0 012 13.5v-3A2.5 2.5 0 014.5 8h1.69c1.397 0 2.785.06 4.15.18m0 8.18a21.413 21.413 0 005.152 1.343c1.17.202 2.348.337 3.535.405v-9.556c-1.187.068-2.365.203-3.535.405-1.7.29-3.418.74-5.152 1.343m0 8.18l-3.34 3.34a1.5 1.5 0 01-2.61-.83l-.36-4.69m9.46-6.62A20.916 20.916 0 0019 12a20.916 20.916 0 00-3.34 2.84" />
                            </svg>
                        </div>
                        
                        <h3 class="text-xl font-extrabold text-primary mb-4 mt-2">Publiez</h3>
                        <p class="text-gray-600 text-[0.95rem] leading-relaxed font-medium">Diffusez vos offres d'emploi IT en quelques clics auprès de notre communauté qualifiée.</p>
                    </div>

                    <!-- Card 2 -->
                    <div class="relative bg-white rounded-2xl border-2 border-accent p-8 pt-16 text-center shadow-[0_10px_30px_rgba(0,119,182,0.08)] hover:-translate-y-2 hover:shadow-[0_15px_40px_rgba(0,119,182,0.15)] transition-all duration-300 fade-in" style="transition-delay: 100ms;">
                        <div class="absolute top-0 left-0 bg-accent text-white font-extrabold text-xl w-12 h-12 flex items-center justify-center rounded-br-2xl rounded-tl-xl shadow-sm">2</div>
                        
                        <div class="absolute -top-12 left-1/2 -translate-x-1/2 w-24 h-24 bg-[#eef5fa] rounded-full border-[6px] border-primary flex items-center justify-center shadow-lg">
                            <svg class="w-10 h-10 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m3.75 9v6m3-3H9m1.5-12H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
                                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75" />
                            </svg>
                        </div>
                        
                        <h3 class="text-xl font-extrabold text-primary mb-4 mt-2">Recevez</h3>
                        <p class="text-gray-600 text-[0.95rem] leading-relaxed font-medium">Obtenez des candidatures ciblées de profils tech correspondant exactement à vos besoins.</p>
                    </div>

                    <!-- Card 3 -->
                    <div class="relative bg-white rounded-2xl border-2 border-accent p-8 pt-16 text-center shadow-[0_10px_30px_rgba(0,119,182,0.08)] hover:-translate-y-2 hover:shadow-[0_15px_40px_rgba(0,119,182,0.15)] transition-all duration-300 fade-in" style="transition-delay: 200ms;">
                        <div class="absolute top-0 left-0 bg-accent text-white font-extrabold text-xl w-12 h-12 flex items-center justify-center rounded-br-2xl rounded-tl-xl shadow-sm">3</div>
                        
                        <div class="absolute -top-12 left-1/2 -translate-x-1/2 w-24 h-24 bg-[#eef5fa] rounded-full border-[6px] border-primary flex items-center justify-center shadow-lg">
                            <svg class="w-10 h-10 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 15.75l-2.489-2.489m0 0a3.375 3.375 0 10-4.773-4.773 3.375 3.375 0 004.774 4.774zM21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 8.25h.008v.008h-.008V8.25zm0 3h.008v.008h-.008v-.008zm0 3h.008v.008h-.008v-.008z" />
                            </svg>
                        </div>
                        
                        <h3 class="text-xl font-extrabold text-primary mb-4 mt-2">Évaluez</h3>
                        <p class="text-gray-600 text-[0.95rem] leading-relaxed font-medium">Triez et analysez les profils grâce à nos outils de matching et d'évaluation avancés.</p>
                    </div>

                    <!-- Card 4 -->
                    <div class="relative bg-white rounded-2xl border-2 border-accent p-8 pt-16 text-center shadow-[0_10px_30px_rgba(0,119,182,0.08)] hover:-translate-y-2 hover:shadow-[0_15px_40px_rgba(0,119,182,0.15)] transition-all duration-300 fade-in" style="transition-delay: 300ms;">
                        <div class="absolute top-0 left-0 bg-accent text-white font-extrabold text-xl w-12 h-12 flex items-center justify-center rounded-br-2xl rounded-tl-xl shadow-sm">4</div>
                        
                        <div class="absolute -top-12 left-1/2 -translate-x-1/2 w-24 h-24 bg-[#eef5fa] rounded-full border-[6px] border-primary flex items-center justify-center shadow-lg">
                            <svg class="w-10 h-10 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z" />
                            </svg>
                        </div>
                        
                        <h3 class="text-xl font-extrabold text-primary mb-4 mt-2">Embauchez</h3>
                        <p class="text-gray-600 text-[0.95rem] leading-relaxed font-medium">Recrutez la perle rare et intégrez le meilleur talent IT à votre équipe.</p>
                    </div>

                </div>
            </div>
        </div>
    </section>

"""

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_section + content[end_idx:]
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("Success")
else:
    print("Markers not found")
