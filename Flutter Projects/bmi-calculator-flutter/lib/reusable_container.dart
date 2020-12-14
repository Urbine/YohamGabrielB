import 'package:flutter/material.dart';

class ContainerCard extends StatelessWidget {
  ContainerCard({@required this.colour, this.cardChild});

  final Color colour;
  final Widget cardChild;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: cardChild,
      margin: EdgeInsets.all(15.0),
      decoration: BoxDecoration(
        color: colour,
        borderRadius: BorderRadiusDirectional.circular(10.0),
      ),
    );
  }
}
