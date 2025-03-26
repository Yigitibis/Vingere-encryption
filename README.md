
# Vigenère Şifreleme Algoritması

Bu proje, Vigenère şifreleme algoritmasını kullanarak metinleri şifrelemek ve çözmek için geliştirilmiştir. Python ile yazılmış olup terminal üzerinden çalıştırılabilir.

## Algoritma Açıklaması

Vigenère şifreleme algoritması, bir **çoklu alfabe şifreleme** tekniğidir. Her harf, bir anahtar kelimeye bağlı olarak belirli bir kaydırma değeri ile şifrelenir. Şifreleme şu şekilde çalışır:

1. Şifrelenecek mesaj ve bir anahtar kelime alınır.
2. Anahtar kelime, mesaj uzunluğuna kadar tekrar edilir.
3. Her harf, ilgili anahtar harfine göre kaydırılarak şifrelenir.
4. Aynı yöntem tersine uygulanarak şifre çözülür.

## Kullanım

### 1. Gereksinimler
Bu programın çalıştırılabilmesi için sisteminizde Python'un kurulu olması gerekir. Python'un yüklü olup olmadığını kontrol etmek için terminale aşağıdaki komutu yazabilirsiniz:

```sh
python --version
veya
```sh
python3 --version
