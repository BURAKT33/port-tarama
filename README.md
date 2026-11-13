# port-tarama

Python `socket` kütüphanesiyle yazılmış basit bir TCP bağlantı kontrolü. Yalnızca size ait veya test etmeye izniniz olan makinelerde kullanın.

Betik `port tarama/porttarama2.py` dosyasındadır. Argüman verilmezse hedef `localhost` olur. Bir makine adı veya adres verilirse onu çözer ve TCP portlarına bağlanmayı dener; bağlantı kabul eden portları yazar.

## Kurulum

```bash
pip install pyfiglet
```

`socket` Python ile birlikte gelir.

## Çalıştırma

Kendi makinenizde:

```bash
python "port tarama/porttarama2.py"
```

İzinli bir hedef vermek için adresi argüman olarak geçirin. `Ctrl+C` taramayı keser.
