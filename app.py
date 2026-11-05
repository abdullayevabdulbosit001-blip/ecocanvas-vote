from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Vaqtinchalik ma'lumotlar bazasi (Rasmlar va SDG lar)
ARTWORKS = {
    "1": {
        "title": "Tabiat Nafasi",
        "author": "Talaba #1",
        "sdg": "SDG 13: Iqlim o'zgarishiga qarshi kurash",
        "sdg_desc": "Global isish va uning tabiatga ta'sirini kamaytirishga qaratilgan harakatlar.",
        "votes": 12,
        "image": "https://picsum.photos/seed/art1/600/400" # Vaqtinchalik rasm
    },
    "2": {
        "title": "Toza Suv – Hayot",
        "author": "Talaba #2",
        "sdg": "SDG 6: Toza suv va sanitariya",
        "sdg_desc": "Suv resurslarini tejash va ifloslanishning oldini olish.",
        "votes": 8,
        "image": "https://picsum.photos/seed/art2/600/400"
    }
}

@app.route('/art/<art_id>')
def art_page(art_id):
    art = ARTWORKS.get(art_id)
    if not art:
        return "Rasm topilmadi", 404
    return render_template('art.html', art=art, art_id=art_id)

@app.route('/vote/<art_id>', methods=['POST'])
def vote(art_id):
    if art_id in ARTWORKS:
        ARTWORKS[art_id]["votes"] += 1
        return jsonify({"success": True, "votes": ARTWORKS[art_id]["votes"]})
    return jsonify({"success": False}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)