import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.teal,
        body: SafeArea(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircleAvatar(
              radius: 50.0,
              backgroundColor: Colors.red,
              backgroundImage: AssetImage('images/yoham.jpg'),
            ),
            Text(
                'Yoham Gabriel Barboza',
                style: TextStyle(
                  fontFamily: 'DancingScript',
                  fontSize: 30.0,
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
            ),
            Text(
              'FLUTTER DEVELOPER',
              style: TextStyle(
                fontFamily: 'SourceSansPro',
                fontSize: 20.0,
                fontWeight: FontWeight.bold,
                color: Colors.teal[100],
                letterSpacing: 2.5,
              ),
            ),
            SizedBox(
              height: 20.0,
              width: 150.0,
              child: Divider(
                color: Colors.teal[100],
              ),
            ),
            Card(
              color: Colors.white,
              margin: EdgeInsets.symmetric(vertical: 10.0, horizontal: 25.0),
              child: ListTile(
                leading: Icon(
                  Icons.phone,
                  color: Colors.teal[900],
                ),
                title: Text(
                  '+506 7012 3456',
                  style: TextStyle(
                    fontFamily: 'SourceSansPro',
                    fontSize: 20.00,
                    color: Colors.teal.shade900,
                  ),
                ),
              )
            ),
            Card(
              margin: EdgeInsets.symmetric(vertical: 10.0, horizontal: 25.0),
              color: Colors.white,
              child: ListTile(
                leading: Icon(
                  Icons.email,
                  color: Colors.teal[900],
                ),
                title: Text(
                  'profgabriel@teachers.org',
                  style: TextStyle(
                      fontFamily: 'SourceSansPro',
                      fontSize: 20.0,
                      color: Colors.teal[900]
                  ),
                ),
              ),
            )
          ],
        )),
      ),
    );
  }
}
