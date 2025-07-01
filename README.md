# 🔐 Caesar Cipher – Prodigy InfoTech Internship Task-01

This repository contains my implementation of the **Caesar Cipher** encryption and decryption algorithm in Python. This task was completed as part of the **Cybersecurity Internship** at **Prodigy InfoTech**.

## 📖 About Caesar Cipher
The Caesar Cipher is a basic encryption technique where each letter in the message is shifted by a fixed number of positions in the alphabet.
- Encryption shifts letters forward
- Decryption shifts letters backward
It’s a simple form of substitution cipher and is mainly used for educational purposes today.

## 📌 What happens to numbers & special characters?
In most implementations:
- Numbers (0–9) and special characters (like !, @, #, etc.) are left unchanged
- They are preserved in their original position during both encryption and decryption

## 📝 Task Description

Create a Python program that:
- Encrypts and decrypts messages using the Caesar Cipher algorithm
- Accepts user input for the message and shift value
- Performs both encryption and decryption based on user selection

## 🛠️ Features

- Simple command-line interface
- Supports uppercase and lowercase letters
- Handles wrap-around for alphabet characters
- Easy to modify or integrate into other Python programs

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Run the Program

```bash
python caesar_cipher.py
