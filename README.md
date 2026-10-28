# Computación Cuántica

Tareas del curso de Computación Cuántica, Programa de Física, Universidad del Quindío.

Autores de las tareas: Daniel Calpa Burbano, Nancy Camacho Santos y Natalia Isabel Martínez Gómez.

En ambas tareas el ejercicio fue reescribir un artículo en español, desarrollando los pasos intermedios de las deducciones, y reproducir numéricamente sus figuras. El contenido científico, los resultados y las figuras originales son de los autores de cada artículo; las tareas no presentan resultados nuevos.

## Tarea 1. Bloqueo de fotones no convencional en QED de cavidad con amplificación paramétrica

Artículo original:

> M. M. Mahana, S. Das y T. N. Dey, *Unconventional photon blockade in cavity QED with parametric amplification*,
> Phys. Rev. A **113**, 013724 (2026). [arXiv:2505.04280](https://arxiv.org/abs/2505.04280) (licencia [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/))

| Archivo | Contenido |
|---|---|
| [`articulo_bloqueo_de_fotones_reescrito.pdf`](tarea1_bloqueo_de_fotones/articulo_bloqueo_de_fotones_reescrito.pdf) | Artículo reescrito con los pasos intermedios. |
| [`figuras_bloqueo_de_fotones.ipynb`](tarea1_bloqueo_de_fotones/figuras_bloqueo_de_fotones.ipynb) | Reproducción de las figuras con QuTiP: función de correlación de segundo orden *g*<sup>(2)</sup>(0) con la cavidad o el átomo bombeados. |

## Tarea 2. Caminatas aleatorias cuánticas: formalismo y fundamentos clásicos

Artículo original:

> E. Ng, *Quantum Random Walks*, Department of Physics, Massachusetts Institute of Technology (2012).
> [PDF](https://web.stanford.edu/~edwin98/qrw-paper.pdf)

| Archivo | Contenido |
|---|---|
| [`caminatas_aleatorias_cuanticas.pdf`](tarea2_caminatas_cuanticas/caminatas_aleatorias_cuanticas.pdf) | Artículo reescrito con los pasos intermedios. |
| [`codigo/caminata_clasica.py`](tarea2_caminatas_cuanticas/codigo/caminata_clasica.py) | Caminata aleatoria clásica con *p* = 0.15, 0.50 y 0.85 (Figura 1). |
| [`codigo/caminata_cuantica_discreta.py`](tarea2_caminatas_cuanticas/codigo/caminata_cuantica_discreta.py) | Caminata cuántica en tiempo discreto con moneda de Hadamard (Figura 3; con la moneda \|+y⟩, Figura 4). |
| [`codigo/caminata_cuantica_continua.py`](tarea2_caminatas_cuanticas/codigo/caminata_cuantica_continua.py) | Caminata cuántica en tiempo continuo: probabilidad en *z* = 10 en función del tiempo (Figura 5). |

El código es el de los anexos del artículo reescrito.

## Requisitos

```
pip install numpy scipy matplotlib qutip
```
