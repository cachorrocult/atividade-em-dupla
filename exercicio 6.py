class AlienGallery:
    def __init__(self, gallery_name, artworks):
        self.gallery_name = gallery_name
        self.artworks = artworks
    def add_item(self, name, value):
        if name.strip() != "" and value > 0:
            self.artworks.append(f"{name}:{value}")
            print("Artwork added with success!")
        else:
            print("Invalid data. Failed to add artwork.")
    def list_items(self):
        print("Registered artworks:")
        for artwork in self.artworks:
            print(artwork)
    def calculate_total(self):
        total = 0
        for artwork in self.artworks:
            parts = artwork.split(":")
            value = int(parts[1])
            total += value
        return total
    def find_most_valuable_item(self):
        if len(self.artworks) == 0:
            return "No artwork registered."
        rarest_artwork = ""
        bigger_value = 0
        for artwork in self.artworks:
            parts = artwork.split(":")
            name = parts[0]
            value = int(parts[1])

            if value > bigger_value:
                bigger_value = value
                rarest_artwork = name
        return f"{rarest_artwork} ({bigger_value})"
    def classify_collection(self):
        total = self.calculate_total()

        if total < 500:
            return "Common gallery"
        elif total <= 1500:
            return "Rare gallery"
        else:
            return "Alien gallery"
    def show_report(self):
        print(f"gallery: {self.gallery_name}")
        print(f"Rarities total: {self.calculate_total()}")
        print(f"Rariest artowrk: {self.find_most_valuable_item()}")
        print(f"Classification: {self.classify_collection()}")
gallery = AlienGallery(
    "Stars Museum",
    [
        "lunar_sculpture:400",
        "cloudy_frame:900",
        "martian_vase:250"
    ]
)
gallery.list_items()
print()
gallery.show_report()
