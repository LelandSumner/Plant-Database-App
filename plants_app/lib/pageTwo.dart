import 'package:flutter/material.dart';
import 'package:plants_app/api/api.dart';
import 'package:provider/provider.dart';
import 'package:plants_app/pageThree.dart';

//Page Two of App
int heightAdjust = 200; //amount of vertical space
int widthAdjust = 75; //amount of horizontal space
double fSize = 30.0; //font Size for Buttons
List<String> colors = [
  'Brown',
  'Dark-Brown',
  'Red-Brown',
  'Light-Green',
  'Green',
  'Red',
  'Red-Green',
  'Purple',
  'Yellow',
  'White',
  'Purple-Blue',
  'Red-Purple',
  'Pink',
  'Green-White',
  'Blue',
  'Orange',
  'Gold'
];

class PageTwo extends StatelessWidget {
  const PageTwo({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(''),
        centerTitle: true,
        backgroundColor: Colors.blue,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
      ),
    );
  }
}

class Grass extends PageTwo {
  const Grass({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    final plantP = Provider.of<PlantProvider>(context);
    return ChangeNotifierProvider(
      create: (context) => PlantProvider(),
      child: Scaffold(
          backgroundColor: Colors.grey[300],
          appBar: AppBar(
            title: Text('Grasses'),
            centerTitle: true,
            backgroundColor: Colors.blue,
          ),
          body: ObjList(plantP.plants)),
    );
  }
}

//search by colors
class Flowers extends PageTwo {
  final String color;

  Flowers(this.color);
  @override
  Widget build(BuildContext context) {
    final flowerP = Provider.of<FlowerProvider>(context);
    return Scaffold(
        appBar: AppBar(
          title: Text('Flowers'),
          centerTitle: true,
          backgroundColor: Colors.blue,
        ),
        body: ObjList(flowerP.flowers
            .where((flower) => (flower.colors.contains(color)))
            .toList()));
  }
}

//search by colors
class Berries extends PageTwo {
  final String color;

  Berries(this.color);
  @override
  Widget build(BuildContext context) {
    final berryP = Provider.of<BerryProvider>(context);
    return Scaffold(
        appBar: AppBar(
          title: Text('Berries'),
          centerTitle: true,
          backgroundColor: Colors.blue,
        ),
        body: ObjList(berryP.berries
            .where((berry) => (berry.colors.contains(color)))
            .toList()));
  }
}

//search by shape
class Leaves extends PageTwo {
  final String init;

  Leaves(this.init);

  @override
  Widget build(BuildContext context) {
    final leafP = Provider.of<LeafProvider>(context);
    return Scaffold(
        appBar: AppBar(
          title: Text('Leaves'),
          centerTitle: true,
          backgroundColor: Colors.blue,
        ),
        body: ObjList(leafP.leaves
            .where((leaf) => (leaf.shape.contains(init)))
            .toList()));
  }
}

//search by invasive/native
class Status extends PageTwo {
  final bool isNative;

  Status(this.isNative);

  @override
  Widget build(BuildContext context) {
    final statP = Provider.of<PlantProvider>(context);
    return Scaffold(
        appBar: AppBar(
          title: Text('Status'),
          centerTitle: true,
          backgroundColor: Colors.blue,
        ),
        body: ObjList(statP.plants
            .where((plant) => (plant.isNative == isNative))
            .toList()));
  }
}

class MyButton extends StatelessWidget {
  final String name;
  final color;
  final Widget nextPage;
  final int howMany;
  const MyButton(this.name, this.color, this.howMany, this.nextPage);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: (MediaQuery.of(context).size.width) - widthAdjust,
      height: ((MediaQuery.of(context).size.height) - heightAdjust) / howMany,
      child: ElevatedButton(
        onPressed: () => Navigator.of(context)
            .push(MaterialPageRoute(builder: (context) => nextPage)),
        style: ButtonStyle(
          backgroundColor: MaterialStateProperty.all(color),
        ),
        child: Text(
          name,
          style: TextStyle(
            fontSize: fSize,
          ),
        ),
      ),
    );
  }
}

class ObjList extends StatelessWidget {
  final obj;

  ObjList(this.obj);

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => PlantProvider(),
      child: ListView.builder(
        itemCount: obj.length,
        itemBuilder: (BuildContext context, int index) {
          return Padding(
            padding: EdgeInsets.fromLTRB(5.0, 6.0, 5.0, 0),
            child: ListTile(
                tileColor: Colors.white,
                title: Text(obj[index].name),
                onTap: () => Navigator.of(context).push(MaterialPageRoute(
                    builder: (context) => PageThree(obj[index].name))),
                trailing: Padding(
                    padding: EdgeInsets.all(4.0),
                    child: Image(
                        image: AssetImage(
                            'assets/images/' + obj[index].imageName)))),
          );
        },
      ),
    );
  }
}

class FlowerColors extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Flower Colors'),
          centerTitle: true,
          backgroundColor: Colors.blue,
        ),
        body: ListView.builder(
            itemCount: colors.length,
            itemBuilder: (BuildContext context, int index) {
              return Padding(
                  padding: EdgeInsets.fromLTRB(30, 10, 30, 0),
                  child: MyButton(
                      colors[index], Colors.green, 10, Flowers(colors[index])));
            }));
  }
}

class BerryColors extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Berry Colors'),
          centerTitle: true,
          backgroundColor: Colors.blue,
        ),
        body: ListView.builder(
            itemCount: colors.length,
            itemBuilder: (BuildContext context, int index) {
              return Padding(
                  padding: EdgeInsets.fromLTRB(30, 10, 30, 0),
                  child: MyButton(
                      colors[index], Colors.green, 10, Berries(colors[index])));
            }));
  }
}

class LeafShapes extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Leaf Shapes'),
          centerTitle: true,
          backgroundColor: Colors.blue,
        ),
        body: ListView.builder(
            itemCount: shapes.length,
            itemBuilder: (BuildContext context, int index) {
              return Padding(
                  padding: EdgeInsets.fromLTRB(30, 10, 30, 0),
                  child: MyButton(shapes[index].name, Colors.green,
                      shapes.length, Leaves(shapes[index].init)));
            }));
  }
}

class CheckStatus extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Status'),
        centerTitle: true,
        backgroundColor: Colors.blue,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            MyButton('Native', Colors.green[900], 2, Status(true)),
            MyButton('Invasive', Colors.red[900], 2, Status(false)),
          ],
        ),
      ),
    );
  }
}
