## Маркировка связных компонент

### P.S
В исходное решение надо было добавить всего лишь
```Python
    for i, j in enumerate(np.unique(labels)):
        labels[labels == j] = i

```
![img](./img.png)