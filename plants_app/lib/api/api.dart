import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../models/plants.dart';

class PlantProvider with ChangeNotifier {
  PlantProvider() {
    this.fetchTasks();
  }

  List<Plant> _plants = [];

  List<Plant> get plants {
    return [..._plants];
  }

  fetchTasks() async {
    String grabData = await rootBundle.loadString('assets/data/Plants.json');
    var data = json.decode(grabData) as List;
    _plants = data.map<Plant>((json) => Plant.fromJson(json)).toList();
  }
}

class FlowerProvider with ChangeNotifier {
  FlowerProvider() {
    this.fetchTasks();
  }

  List<Flower> _flowers = [];

  List<Flower> get flowers {
    return [..._flowers];
  }

  fetchTasks() async {
    String grabData = await rootBundle.loadString('assets/data/Flowers.json');
    var data = json.decode(grabData) as List;
    _flowers = data.map<Flower>((json) => Flower.fromJson(json)).toList();
  }
}

class BerryProvider with ChangeNotifier {
  BerryProvider() {
    this.fetchTasks();
  }

  List<Berry> _berries = [];

  List<Berry> get berries {
    return [..._berries];
  }

  fetchTasks() async {
    String grabData = await rootBundle.loadString('assets/data/Berries.json');
    var data = json.decode(grabData) as List;
    _berries = data.map<Berry>((json) => Berry.fromJson(json)).toList();
  }
}

class LeafProvider with ChangeNotifier {
  LeafProvider() {
    this.fetchTasks();
  }

  List<Leaf> _leaves = [];

  List<Leaf> get leaves {
    return [..._leaves];
  }

  fetchTasks() async {
    String grabData = await rootBundle.loadString('assets/data/Leaves.json');
    var data = json.decode(grabData) as List;
    _leaves = data.map<Leaf>((json) => Leaf.fromJson(json)).toList();
  }
}

class StemProvider with ChangeNotifier {
  StemProvider() {
    this.fetchTasks();
  }

  List<Stem> _stems = [];

  List<Stem> get stems {
    return [..._stems];
  }

  fetchTasks() async {
    String grabData = await rootBundle.loadString('assets/data/Stems.json');
    var data = json.decode(grabData) as List;
    _stems = data.map<Stem>((json) => Stem.fromJson(json)).toList();
  }
}
