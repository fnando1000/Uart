String mensaje = "hola mundo";
int desplazamiento = 3;

String cifradoCesar(String texto, int desplazamiento) {
  String resultado = "";
  for (int i = 0; i < texto.length(); i++) {
    char c = texto[i];
    if (isAlpha(c)) {
      char base = isUpperCase(c) ? 'A' : 'a';
      c = (c - base + desplazamiento) % 26 + base;
    }
    resultado += c;
  }
  return resultado;
}

void setup() {
  Serial.begin(9600);
  delay(2000); // Esperar a que se establezca la conexión
  String cifrado = cifradoCesar(mensaje, desplazamiento);
  Serial.println(cifrado);
}

void loop() {
  // No hacemos nada más
}

