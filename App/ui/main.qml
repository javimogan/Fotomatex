import QtQuick 2.6
import QtQuick.Window 2.2
import QtQuick.Controls 1.4



Window {

    id: window
    visible: true
    color: "#dddddd"
    width: Screen.desktopAvailableWidth
    height: Screen.desktopAvailableHeight
    title: qsTr("Fotomatex")


    //Poner en pantalla completa
    onAfterRendering: {
        window.visibility = Window.FullScreen;
    }


    MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.LeftButton | Qt.RightButton
        onClicked: {
            if (mouse.button === Qt.RightButton)
                contextMenu.popup()
        }
        onPressAndHold: {
            if (mouse.source === Qt.MouseEventNotSynthesized)
                contextMenu.popup()
        }

        Menu {
            id: contextMenu
            objectName: "context"
            MenuItem {
                signal clicked()
                id:ruta;
                objectName: "btnCambiarRuta"
                text: "Cambiar ruta destino"
                shortcut: "Ctrl+X"
                onTriggered: {
                    clicked()
                }


            }
            MenuItem {
                id:salir;
                objectName: "btnSalir"
                text: "Salir"
                onTriggered: {
                    Qt.quit()
                }
                shortcut: "Ctrl+Z"

            }
        }
    }



    Rectangle {
        id: background
        anchors.fill: parent;
        color: "#343434"
        x: 0
        y: 0
        Image {
            id: image;
            clip: false;
            source: "inicio/fondo.jpg";
            fillMode: Image.PreserveAspectCrop;
            anchors.fill: parent;
            opacity: 1;
            width: Window.width;
            height: Window.height;

            Image {
                id: logo
                x: Window.width-width - 10;
                y: Window.height-height - 10;
                fillMode: Image.PreserveAspectFit
                clip: false
                source: "inicio/icon.png"
            }

//            Text {
//                id: version
//                x: Window.width-width - 10;
//                y: Window.height-height - 10;
//                //width: 386
//                //height: 47
//                color: "#ffffff"
//                text: qsTr("@javimogan")
//                font.bold: false
//                font.pixelSize: 24
//            }

        }


    }

    Column {
        id: fotos
        objectName: "contenedor_fotos"
        x: 0
        y: 0
        width: Window.width/3
        height: window.height

        Row {
            id: row
            objectName: "caja1"
            width: parent.width
            height: (parent.height/3)

            Image {
                objectName: "imagen1"
                id: image2
                width: parent.width
                height:parent.height
                fillMode: Image.PreserveAspectFit
                clip: false
                source: "inicio/1.png"
            }
        }

        Row {
            id: row1
            objectName: "caja2"
            width: parent.width
            height: (parent.height/3)

            Image {
                id: image3
                width: parent.width
                height:parent.height
                fillMode: Image.PreserveAspectFit
                objectName: "imagen2"
                clip: false
                source: "inicio/2.png"
            }
        }

        Row {
            id: row2
            objectName: "caja3"
            width: parent.width
            height: (parent.height/3)

            Image {
                id: image4
                width: parent.width
                height:parent.height
                fillMode: Image.PreserveAspectFit
                objectName: "imagen3"
                clip: false
                source: "inicio/3.png"
            }
        }


    }

    Column {
        id: column1
        x: Window.width/3
        y: 0
        width: Window.width-Window.width/3
        height: Window.height

        Text {
            objectName: "title"
            id: text1
            color: "#ffffff"
            text: qsTr("Pulsa el botón")
            anchors.horizontalCenter: parent.horizontalCenter
            y: 10;
            font.pixelSize: 130
            wrapMode: Text.NoWrap
            renderType: Text.QtRendering
            horizontalAlignment: Text.AlignHCenter
        }

        Row {
            visible: true
            id: row3
            width: parent.width/1.5
            height: parent.height/1.5
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter

            Image {
                id: image5
                height:parent.height
                visible: true
                fillMode: Image.PreserveAspectFit
                objectName: "imagen4"
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                source: "inicio/4.png"

                onVisibleChanged: {
                    text2.visible =  !text2.visible
                }
            }
        }
    }

    Text {
        id: text2
        objectName: "counter"
        color: "#ffffff"
        text: qsTr("5")
        visible: false
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        font.pixelSize: 500
    }

    Rectangle {
        id: camaraConectada
        objectName: "controlCamara"
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        width: 1066
        height: 410
        color: "#f72727"

        Text {
            id: text3
            anchors.horizontalCenter: parent.horizontalCenter
            y: 22
            width: 771
            text: qsTr("Conecte la camara.")
            textFormat: Text.RichText
            font.pixelSize: 80
        }

        Image {
            id: image1
            x: 407
            y: 135
            width: 254
            height: 237
            clip: false
            source: "inicio/nocamera.png"
        }
    }

    Rectangle {
        id: arduinoConectado
        objectName: "controlBoton"
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        width: 1066
        height: 410
        color: "#f72727"
        Text {
            id: text4
            anchors.horizontalCenter: parent.horizontalCenter
            y: 22
            width: 771
            text: qsTr("Conecte el pulsador.")
            textFormat: Text.RichText
            font.pixelSize: 80
        }

        Image {
            id: image6
            x: 407
            y: 135
            width: 254
            height: 237
            source: "inicio/pulsador.jpeg"
            clip: false
        }
    }

}

/*##^##
Designer {
    D{i:22;invisible:true}
}
##^##*/
