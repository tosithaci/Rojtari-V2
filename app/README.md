🛡️ Rojtari V2: Multi-Threaded System Monitor
Një platformë monitorimi e bazuar në Docker, e ndërtuar për të mbikëqyrur gjendjen e pajisjeve në rrjet në kohë reale. Ky projekt demonstron parimet e automatizimit, infrastrukturës si kod (IaC) dhe monitorimit dinamik.

🚀 Veçoritë Kryesore
Paralelizëm me Multi-threading: Përdor ThreadPoolExecutor për të kryer kontrollet (pings) e të gjitha pajisjeve njëkohësisht.

Njoftime Inteligjente: Integrim me Telegram API për të dërguar njoftime vetëm kur ndryshon statusi i një pajisjeje (Delta Monitoring).

Dashboard Live: Faqe Web interaktive me Chart.js që tregon statistikat "Online vs Offline" në kohë reale.

Infrastrukturë Docker: Konfigurim me dy kontejnerë (Python & Nginx) me Healthchecks për vetë-shërim (Self-healing).

🛠️ Arkitektura
Projekti funksionon përmes një rrjeti të izoluar në Docker:

Backend (Python): Ekzekuton monitorimin dhe shkruan të dhënat në një volum të ndarë (shared_data).

Frontend (Nginx): Shërben skedarët statikë (HTML/JS) dhe lexon të dhënat live nga volumi.