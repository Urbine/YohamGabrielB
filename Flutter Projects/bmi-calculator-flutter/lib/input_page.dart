import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'reusable_container.dart';
import 'container_card.dart';

const bottomContainerHeight = 80.0;
const startColour = Color(0xFF1D1E33);
const bottomContainerColour = Color(0xFFEB1555);
const inactiveCardColour = Color(0xFF111328);

class InputPage extends StatefulWidget {
  @override
  _InputPageState createState() => _InputPageState();
}

Color maleCardColour = inactiveCardColour;
Color femaleCardColour = inactiveCardColour;

// male = 1 female = 2
void updateCardColour(int gender) {
  // if male is pressed
  if (gender == 1) {
    if (maleCardColour == inactiveCardColour) {
      maleCardColour = startColour;
      femaleCardColour = inactiveCardColour;
    } else {
      maleCardColour = inactiveCardColour;
    }
  }
  // if female is pressed
  if (gender == 2) {
    if (femaleCardColour == inactiveCardColour) {
      femaleCardColour = startColour;
      maleCardColour = inactiveCardColour;
    } else {
      femaleCardColour = inactiveCardColour;
    }
  }
}

class _InputPageState extends State<InputPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('BMI CALCULATOR'),
      ),
      body: Column(
        children: [
          Expanded(
            child: Row(
              children: [
                Expanded(
                  child: GestureDetector(
                    onTap: () {
                      setState(() {
                        updateCardColour(1);
                      });
                    },
                    child: ContainerCard(
                      colour: maleCardColour,
                      cardChild: ReusableContainer(
                        label: 'MALE',
                        icon: FontAwesomeIcons.mars,
                      ),
                    ),
                  ),
                ),
                Expanded(
                  child: GestureDetector(
                    onTap: () {
                      setState(() {
                        updateCardColour(2);
                      });
                    },
                    child: ContainerCard(
                      colour: femaleCardColour,
                      cardChild: ReusableContainer(
                        label: 'FEMALE',
                        icon: FontAwesomeIcons.venus,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
          Expanded(
            child: ContainerCard(
              colour: startColour,
            ),
          ),
          Expanded(
            child: Row(
              children: [
                Expanded(
                  child: ContainerCard(
                    colour: startColour,
                  ),
                ),
                Expanded(
                  child: ContainerCard(
                    colour: startColour,
                  ),
                ),
              ],
            ),
          ),
          Container(
            color: bottomContainerColour,
            margin: EdgeInsets.only(top: 10.0),
            height: bottomContainerHeight,
            width: double.infinity,
          ),
        ],
      ),
    );
  }
}
