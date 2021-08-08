import 'package:flutter/material.dart';
import 'package:plants_app/api/api.dart';
import 'package:plants_app/pageTwo.dart';
import 'package:provider/provider.dart';

int heightAdjust = 200; //amount of vertical space
int widthAdjust = 75; //amount of horizontal space
double fSize = 30.0; //font Size for Buttons
void main() {
  runApp(MultiProvider(
      providers: [
        ChangeNotifierProvider<PlantProvider>(
            create: (context) => PlantProvider()),
        ChangeNotifierProvider<BerryProvider>(
            create: (context) => BerryProvider()),
        ChangeNotifierProvider<FlowerProvider>(
            create: (context) => FlowerProvider()),
        ChangeNotifierProvider<LeafProvider>(
            create: (context) => LeafProvider()),
        ChangeNotifierProvider<StemProvider>(
            create: (context) => StemProvider()),
      ],
      child: MaterialApp(
        title: 'Plant App',
        home: Home(),
      )));
}

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Plants Home'),
        centerTitle: true,
        backgroundColor: Colors.green,
      ),
      body: Center(
        child:
            Column(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          MyButton('Grass', Colors.green[900], 5, Grass()),
          MyButton('Berry/Seed', Colors.redAccent[700], 5, BerryColors()),
          MyButton('Flower', Colors.amber[800], 5, FlowerColors()),
          MyButton('Leaf', Colors.blue[900], 5, LeafShapes()),
          MyButton('Status', Colors.grey[900], 5, CheckStatus()),
        ]),
      ),
    );
  }
}
