import 'package:flutter/material.dart';
import 'package:plants_app/api/api.dart';
import 'package:provider/provider.dart';
import 'models/plants.dart';

double height = 100; //amount of vertical space
double width = 100; //amount of horizontal space
List<Shapes> shapes = [
  new Shapes('Arrow-Shaped', 'AR'),
  new Shapes('Compound', 'CP'),
  new Shapes('Deltoid', 'DL'),
  new Shapes('Heart-Shaped', 'HT'),
  new Shapes('Lanecolate', 'LA'),
  new Shapes('Linear', 'LI'),
  new Shapes('Lobed', 'LB'),
  new Shapes('Oblong', 'OB'),
  new Shapes('Oval', 'OL'),
  new Shapes('Three-leaved', 'TL')
];

class PageThree extends StatelessWidget {
  final String plant;

  PageThree(this.plant);

  @override
  Widget build(BuildContext context) {
    final plantP = Provider.of<PlantProvider>(context);
    final flowerP = Provider.of<FlowerProvider>(context);
    final berryP = Provider.of<BerryProvider>(context);
    final leafP = Provider.of<LeafProvider>(context);
    final stemP = Provider.of<StemProvider>(context);
    final fullPlant =
        new FullPlant(plantP, flowerP, berryP, leafP, stemP, this.plant);
    return Scaffold(
        backgroundColor: Colors.grey[300],
        appBar: AppBar(
          title: Text(plant.toUpperCase()),
          centerTitle: true,
          backgroundColor: Colors.red,
        ),
        body: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: fullPlant.images),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Padding(
                  padding: const EdgeInsets.only(left: 10.0),
                  child: Text('Name: ' + fullPlant.name),
                ),
                Padding(
                  padding: const EdgeInsets.only(left: 10.0),
                  child: Text('Latin Name: ' + fullPlant.latinName),
                ),
              ],
            ),
            Padding(
              padding: const EdgeInsets.only(left: 10.0),
              child: Text('Status: ' + fullPlant.status),
            ),
            Padding(
              padding: const EdgeInsets.only(left: 10.0),
              child: Text('Height: ' + fullPlant.height),
            ),
            Padding(
              padding: const EdgeInsets.only(left: 10.0),
              child: Text('Stem: ' + fullPlant.stemDesc),
            ),
            Padding(
              padding: const EdgeInsets.only(left: 10.0),
              child: Text('Leaves: ' + fullPlant.leafDesc),
            ),
            Padding(
              padding: const EdgeInsets.only(left: 10.0),
              child: Text('Flower: ' + fullPlant.flowerDesc),
            ),
            Padding(
              padding: const EdgeInsets.only(left: 10.0),
              child: Text('Seeds: ' + fullPlant.berryDesc),
            )
          ],
        ));
  }
}

class FullPlant {
  late String name;
  late String latinName;
  late String status;
  late String height;
  String flowerDesc = '';
  String berryDesc = '';
  String leafDesc = '';
  String stemDesc = '';
  List<Widget> images = [];

  FullPlant(PlantProvider plantP, FlowerProvider flowerP, BerryProvider berryP,
      LeafProvider leafP, StemProvider stemP, String plantName) {
    Plant plant = plantP.plants.where((plant) => plant.name == plantName).first;

    name = plantName;
    latinName = plant.latinName;
    images.add(ClickabelPicture(plant.imageName));
    status = plant.isNative ? 'Native' : 'Invasive';
    height = plant.height;
    var vrbl;
    Iterable varList = berryP.berries.where((berry) => berry.name == plantName);
    if (varList.isNotEmpty) {
      vrbl = varList.first;
      berryDesc = vrbl.colors + ', ' + vrbl.desc;
      if (vrbl.imageName != 'None.jpg')
        images.add(ClickabelPicture(vrbl.imageName));
    }
    varList = flowerP.flowers.where((flower) => flower.name == plantName);
    if (varList.isNotEmpty) {
      vrbl = varList.first;
      flowerDesc = vrbl.colors + ', ' + vrbl.desc;
      if (vrbl.imageName != 'None.jpg')
        images.add(ClickabelPicture(vrbl.imageName));
    }
    varList = leafP.leaves.where((leaf) => leaf.name == plantName);
    if (varList.isNotEmpty) {
      vrbl = varList.first;
      leafDesc = vrbl.desc;
      for (int i = 0; i < shapes.length; i++) {
        if (shapes[i].init == vrbl.shape)
          leafDesc = shapes[i].name + ', ' + leafDesc;
      }
      if (vrbl.imageName != 'None.jpg')
        images.add(ClickabelPicture(vrbl.imageName));
    }
    varList = stemP.stems.where((stem) => stem.name == plantName);
    if (varList.isNotEmpty) {
      vrbl = varList.first;
      stemDesc = vrbl.desc;
    }
  }
}

class ClickabelPicture extends StatelessWidget {
  final String imageName;

  ClickabelPicture(this.imageName);

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () => Navigator.of(context)
          .push(MaterialPageRoute(builder: (context) => Picture(imageName))),
      child: Container(
        width: width,
        height: height,
        child: Padding(
            padding: EdgeInsets.all(5.0),
            child: Image(image: AssetImage('assets/images/' + imageName))),
      ),
    );
  }
}

class Picture extends StatelessWidget {
  final String image;

  Picture(this.image);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.grey[300],
        appBar: AppBar(
          title: Text(image.toUpperCase()),
          centerTitle: true,
          backgroundColor: Colors.green,
        ),
        body: Center(child: Image(image: AssetImage('images/' + image))));
  }
}

class Shapes {
  String init;
  String name;

  Shapes(this.name, this.init);
}
