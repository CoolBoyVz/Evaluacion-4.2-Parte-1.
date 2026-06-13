# Visualización de Datos X-Y con Flask

## Descripción
Este es mi proyecto personal para la Evaluación Sumativa 4.2 de la asignatura Desarrollo de Software para Hardware (DCSH01).

## Objetivo
[cite_start]El sistema recibe datos X e Y desde una aplicación móvil (APK) y los representa visualmente en una página web utilizando Flask

## Características Técnicas
* [cite_start]Desarrollado con Flask, HTML y CSS.
* [cite_start]El estilo CSS está integrado directamente en la cabecera (`<head>`) utilizando únicamente selectores de ID (`#`).
* [cite_start]Se implementó una matriz personalizada superior a 4x4 para visualizar la posición.


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣤⠤⠤⠴⠤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠲⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⢀⣄⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⣾⣠⠎⠀⣸⠁⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠃⣾⣿⡏⠀⢰⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⠷⠻⠟⠀⠀⠸⣿⠏⠀⠀⢠⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀
⢠⡴⢦⣤⣄⠀⡇⠀⠀⠀⢰⣶⣶⡄⠀⠀⠀⠈⠛⠛⠯⠿⠃⠀⠀⠀⠀⠀⠀⢸⡘⠀⠀
⢸⣹⢿⣾⣹⢿⣿⠀⠀⠀⠀⠹⠏⠀⠀⠀⠀⠀⠀⠀⣀⣶⣆⣀⠀⠀⠀⠀⠀⠀⣿⡀⠀
⠘⣭⢷⣫⡽⣯⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢶⣻⠽⣶⣫⣟⣷⡄⠀⠀⠀⠀⠘⢖⡀
⠀⠘⣯⢷⣻⣽⣻⣿⡄⠀⠀⠀⠀⠀⠀⢀⣼⣳⣻⢞⣟⣳⡽⣞⣳⢿⡀⠀⠀⠀⠀⠘⣡
⠀⠀⠈⢯⢷⣞⣷⣻⣿⣄⠀⠀⠀⠀⢠⣿⣳⡽⣳⣟⣾⡳⣿⠽⣯⣟⣧⠀⠀⠀⠀⠀⠸
⠀⠀⠀⠀⠙⢞⣾⣳⢿⣿⣷⢤⠀⠈⢿⣳⣳⢟⣳⡽⣶⣻⣽⡻⣗⣯⠷⡄⠀⠀⠀⠀⡬
⠀⠀⠀⠀⠀⠀⠱⢏⣿⡿⠁⠀⠉⠶⣸⣷⢏⡿⣷⢿⢷⡿⣶⢿⣹⡎⠁⠈⠳⠶⠶⠊⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠫⣿⣝⡷⣯⠿⣝⣯⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
