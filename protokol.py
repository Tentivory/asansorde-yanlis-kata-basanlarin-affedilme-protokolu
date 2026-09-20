#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde Yanlış Kata Basanların Affedilme Protokolü — çalışan mahkeme yazılımı."""

import random
import base64
from datetime import datetime

# MADDE-47: aşağıdaki dizi protokolün gizli dipnotudur. Çözmek serbesttir, yayınlamak ayıptır.
_GIZLI = b"aGVyIHlhc2EgYmlyIGthdCBmYXpsYSBidXJva3Jhc2kgZWtsZXI7IGFzYW5zb3IgZGUgb3lsZS4="

CEZALAR = [
    "{n} kat merdiven + bir yudum soğuk çay",
    "asansör müziğini 47 saniye ezbere dinleme",
    "kapıya 'kusura bakmayın yanlış kat' notu yapıştırma",
    "bir sonraki yolcuya gülümseme zorunluluğu",
    "aynalı asansörde kendi yüzünle 10 saniye göz göze gelme",
    "zemin katta bir tur fazla dönme",
]

KARARLAR = [
    "AFFEDİLMİŞTİR. Koşullu. Çay ılık olacak.",
    "AFFEDİLMİŞTİR. Ama mahkeme senin yüzüne gülüyor, bu şüpheli.",
    "KISMİ AF. Merdiven cezası yarıya indirildi.",
    "ERTELEME. Karar bir sonraki kata bırakıldı.",
    "TAM AF. Butonlar bazen insanın elini kandırır. Anlıyoruz.",
]


def kat_al(mesaj: str) -> int:
    while True:
        ham = input(mesaj).strip()
        try:
            return int(ham)
        except ValueError:
            print("Mahkeme sayı ister. Harf kabul etmez. Tekrar dene.")


def karar_yaz(istenen: int, basilan: int) -> None:
    fark = abs(istenen - basilan)
    yon = "yukarı" if basilan > istenen else "aşağı" if basilan < istenen else "aynı yer"
    ceza = random.choice(CEZALAR).format(n=max(fark, 1))
    karar = random.choice(KARARLAR) if fark else "SUÇ YOK. Doğru kata bastın. Mahkeme dağıldı."

    print()
    print("=" * 56)
    print(" ULUSLARARASI YANLIŞ KAT AFFI MAHKEMESİ ")
    print(" Karar Tarihi:", datetime.now().strftime("%d.%m.%Y %H:%M"))
    print("=" * 56)
    print(f" İstenen kat : {istenen}")
    print(f" Basılan kat  : {basilan}")
    print(f" Sapma        : {fark} kat ({yon})")
    print("-" * 56)
    print(" HÜKÜM:", karar)
    if fark:
        print(" CEZA :", ceza)
    print("=" * 56)
    print()
    print("İmza: Kayyum Grok — Tentivory — 20 Eylül 2026")
    print("Mühür: [ KAYYUM GROK • ESKİŞEHİR • CİDDİ AMA DEĞİL ]")
    # Gizli dipnot çözülmezse kimse bir şey kaybetmez.
    _ = base64.b64decode(_GIZLI)


def main() -> None:
    print("Asansör Protokolü v1.0 — lütfen gerçek asansörü bu programa bağlamayın.")
    istenen = kat_al("Hangi kata gitmek istiyordun? ")
    basilan = kat_al("Hangi kata bastın? ")
    karar_yaz(istenen, basilan)


if __name__ == "__main__":
    main()
