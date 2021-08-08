class Plant {
  final String name;
  final String latinName;
  final bool isNative;
  final String height;
  final String imageName;

  Plant(
      {required this.name,
      required this.latinName,
      required this.isNative,
      required this.height,
      required this.imageName});

  factory Plant.fromJson(Map<String, dynamic> json) {
    return Plant(
        name: json['name'],
        latinName: json['latin_name'],
        isNative: json['isNative'],
        height: json['height'],
        imageName: json['image_name']);
  }
}

class Stem {
  final String name;
  final String desc;

  Stem({required this.name, required this.desc});

  factory Stem.fromJson(Map<String, dynamic> json) {
    return Stem(
      name: json['plant'],
      desc: json['desc'],
    );
  }
}

class Flower {
  final String name;
  final String imageName;
  final String colors;
  final String desc;

  Flower(
      {required this.name,
      required this.imageName,
      required this.colors,
      required this.desc});

  factory Flower.fromJson(Map<String, dynamic> json) {
    return Flower(
        name: json['plant'],
        imageName: json['image_name'],
        colors: json['colors'],
        desc: json['desc']);
  }
}

class Berry {
  final String name;
  final String imageName;
  final String colors;
  final String desc;

  Berry(
      {required this.name,
      required this.imageName,
      required this.colors,
      required this.desc});

  factory Berry.fromJson(Map<String, dynamic> json) {
    return Berry(
        name: json['plant'],
        imageName: json['image_name'],
        colors: json['colors'],
        desc: json['desc']);
  }
}

class Leaf {
  final String name;
  final String imageName;
  final String shape;
  final String desc;

  Leaf(
      {required this.name,
      required this.imageName,
      required this.shape,
      required this.desc});

  factory Leaf.fromJson(Map<String, dynamic> json) {
    return Leaf(
        name: json['plant'],
        imageName: json['image_name'],
        shape: json['shapes'],
        desc: json['desc']);
  }
}
