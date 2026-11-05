from flask import Flask, render_template_string

app = Flask(__name__)

# Bitta asosiy sahifa uchun HTML shablon (Minimalist va qora-oq dizaynda)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcoCanvas - SDG Brief</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
    </style>
</head>
<body class="bg-white text-black min-h-screen flex flex-col justify-between p-6 md:p-12">
    
    <!-- Header -->
    <header class="max-w-2xl mx-auto w-full text-center py-6">
        <h1 class="text-3xl md:text-4xl font-light tracking-wider uppercase">EcoCanvas</h1>
        <p class="text-xs uppercase tracking-widest text-gray-500 mt-2">Art for Climate Action</p>
    </header>

    <!-- Main Content -->
    <main class="max-w-xl mx-auto w-full space-y-8 my-auto">
        <div class="border-t border-b border-black py-8 space-y-6">
            <h2 class="text-xl font-semibold tracking-wide">SDG haqida qisqacha (Brief)</h2>
            <p class="text-gray-800 leading-relaxed font-light">
                Barqaror Rivojlanish Maqsadlari (BRM / SDG) — bu Birlashgan Millatlar Tashkilotiga a'zo davlatlar tomonidan global muammolarni hal qilish, jumladan iqlim o'zgarishiga qarshi kurashish, ekologik muvozanatni saqlash va kelajak avlod uchun toza sayyorani qoldirish maqsadida qabul qilingan global dasturdir.
            </p>
            <p class="text-gray-800 leading-relaxed font-light">
                Ushbu ko'rgazma san'at orqali jamiyat e'tiborini ekologik muammolarga qaratish va iqlim o'zgarishiga qarshi kurashda har birimizning mas'uliyatimiz borligini eslatishga bag'ishlangan.
            </p>
        </div>

        <div class="text-center text-sm text-gray-500">
            <p>Tashrifingiz uchun rahmat!</p>
        </div>
    </main>

    <!-- Footer -->
    <footer class="max-w-2xl mx-auto w-full text-center text-xs text-gray-400 py-4">
        &copy; 2026 EcoCanvas SDG Initiative.
    </footer>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
