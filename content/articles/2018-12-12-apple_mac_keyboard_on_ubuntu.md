Title: Configurer un clavier Apple Mac sous Ubuntu
Date: 2018-12-12 23:14
Category: OSes
Description: Configuration d'un clavier filaire de Mac (avec pavé numérique) sous Ubuntu 18.04 LTS.

Le clavier Mac n'est toujours pas reconnu correctement dans la version 18.04 LTS d'Ubuntu et ça dure depuis un moment déjà.
En cause, le module `hid_apple` du kernel GNU/Linux qui ne distingue pas correctement la disposition du clavier, ça ne touche pas que Ubuntu mais bien l'ensemble des distributions.

Ca entraine des problèmes bien génants, les touches sont inversées ou n'ont pas le comportement attendu.
Les instructions contenues dans cet article sont valides pour Ubuntu et Debian. Dans le cas d'une autre distribution, adapter la configuration de la [méthode de saisie](#methode-de-saisie) par l'utilitaire le plus adapté. 


Méthode de saisie
-----------------

Configurer les paramètres de saisie de texte, soit avec l'utiltaire "Saisie de texte" / "Keyboard Layouts" ou directement via le terminal dans `/etc/default/keyboard` en y définissant les valeurs suivantes :

```sh
XKBMODEL="pc105"  # Generic 105-key PC (intl.)
XKBLAYOUT="fr"    # French
XKBVARIANT="mac"  # French (Macintosh)
```

Puis appliquer les changements :

```sh
sudo dpkg-reconfigure -f noninteractive keyboard-configuration
```

Disposition des touches
-----------------------

En Europe, on utilise habituellement le standard ISO pour nos claviers. Mais là il faut le désactiver.

```sh
echo 0 | sudo tee /sys/module/hid_apple/parameters/iso_layout
```

Invertion des touches Cmd et Alt
--------------------------------

```sh
echo 1 | sudo tee /sys/module/hid_apple/parameters/swap_opt_cmd
```

Comportement des touches de fonction
------------------------------------

- **0** - Désactive complètement la touche `fn`.
- **1** - Activé par défaut. La touche `F8` déclenche l'action play/pause. `fn + F8` déclenche `F8`.
- **2** - Désactivé par défaut. La touche `F8` déclenche `F8`. `fn + F8` déclenche l'action play/pause.

```sh
echo 2 | sudo tee /sys/module/hid_apple/parameters/fnmode
```

Persister les changements
-------------------------

Pour que ces changements survivent au prochain reboot, il faut les persister dans modprobe et regénérer l'initramfs :

```sh
echo options hid_apple iso_layout=0 | sudo tee -a /etc/modprobe.d/hid_apple.conf
echo options hid_apple swap_opt_cmd=0 | sudo tee -a /etc/modprobe.d/hid_apple.conf
echo options hid_apple fnmode=2 | sudo tee -a /etc/modprobe.d/hid_apple.conf

sudo update-initramfs -u -k all
```

