# Computación Cuántica

Tareas del curso de Computación Cuántica, Programa de Física, Universidad del Quindío.

Autores de las tareas: Daniel Calpa Burbano, Nancy Camacho Santos y Natalia Isabel Martínez Gómez.

Las tareas reproducen numéricamente resultados de artículos publicados; el contenido científico y los resultados originales son de sus autores, y las tareas no presentan resultados nuevos.

## Tarea 1. Bloqueo de fotones no convencional en QED de cavidad con amplificación paramétrica

Artículo original:

> M. M. Mahana, S. Das y T. N. Dey, *Unconventional photon blockade in cavity QED with parametric amplification*,
> Phys. Rev. A **113**, 013724 (2026). [arXiv:2505.04280](https://arxiv.org/abs/2505.04280) (licencia [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/))

| Archivo | Contenido |
|---|---|
| [`articulo_bloqueo_de_fotones_reescrito.pdf`](https://raw.githubusercontent.com/natmart1/Computacion-Cuantica/main/tarea1_bloqueo_de_fotones/articulo_bloqueo_de_fotones_reescrito.pdf) | Artículo reescrito con los pasos intermedios. |
| [`figuras_bloqueo_de_fotones.ipynb`](tarea1_bloqueo_de_fotones/figuras_bloqueo_de_fotones.ipynb) | Reproducción de las figuras con QuTiP: función de correlación de segundo orden *g*<sup>(2)</sup>(0) con la cavidad o el átomo bombeados. |

## Tarea 2. Cálculos de caminatas aleatorias clásicas y cuánticas

Cálculos numéricos de caminatas aleatorias en una dimensión: la caminata clásica y su distribución binomial, la caminata cuántica en tiempo discreto con moneda de Hadamard y la caminata cuántica en tiempo continuo. Las figuras reproducen las de E. Ng, *Quantum Random Walks*, MIT (2012) ([PDF](https://web.stanford.edu/~edwin98/qrw-paper.pdf)).

| Archivo | Contenido |
|---|---|
| [`codigo/caminata_clasica.py`](tarea2_caminatas_cuanticas/codigo/caminata_clasica.py) | Caminata aleatoria clásica con *p* = 0.15, 0.50 y 0.85 (Figura 1). |
| [`codigo/caminata_cuantica_discreta.py`](tarea2_caminatas_cuanticas/codigo/caminata_cuantica_discreta.py) | Caminata cuántica en tiempo discreto con moneda de Hadamard (Figura 3; con la moneda \|+y⟩, Figura 4). |
| [`codigo/caminata_cuantica_continua.py`](tarea2_caminatas_cuanticas/codigo/caminata_cuantica_continua.py) | Caminata cuántica en tiempo continuo: probabilidad en *z* = 10 en función del tiempo (Figura 5). |

## Requisitos

```
pip install numpy scipy matplotlib qutip
```
