```
In [1]: import algotom.io.loadersaver as loco

In [2]: loco.get_hdf_tree("/home/xf31id/Downloads/68067.nxs");
 entry1
    │
    ├── before_scan
    │   │
    │   ├── cam1
    │   │   │
    │   │   ├── cam1_roll (1,)
    │   │   ├── cam1_x (1,)
    │   │   └── cam1_z (1,)
    │   ├── dcm1_cap_1
    │   │   └── dcm1_cap_1 (1,)
    │   ├── dcm1_cap_2
    │   │   └── dcm1_cap_2 (1,)
    │   ├── f1 (1, 1)
    │   ├── f2 (1, 1)
    │   ├── mc1_bragg
    │   │   └── mc1_bragg (1,)
    │   ├── mc2
    │   │   │
    │   │   ├── mc2_bragg (1,)
    │   │   └── mc2_z (1,)
    │   ├── mc2_bragg
    │   │   └── mc2_bragg (1,)
    │   ├── s1
    │   │   │
    │   │   ├── s1_bottom (1,)
    │   │   ├── s1_in (1,)
    │   │   ├── s1_out (1,)
    │   │   ├── s1_t1 (1,)
    │   │   ├── s1_t2 (1,)
    │   │   ├── s1_top (1,)
    │   │   ├── s1_xc (1,)
    │   │   ├── s1_xs (1,)
    │   │   ├── s1_yc (1,)
    │   │   └── s1_ys (1,)
    │   ├── s2
    │   │   │
    │   │   ├── s2_bottom (1,)
    │   │   ├── s2_in (1,)
    │   │   ├── s2_out (1,)
    │   │   ├── s2_top (1,)
    │   │   ├── s2_xc (1,)
    │   │   ├── s2_xs (1,)
    │   │   ├── s2_yc (1,)
    │   │   └── s2_ys (1,)
    │   ├── s3
    │   │   │
    │   │   ├── s3_bottom (1,)
    │   │   ├── s3_in (1,)
    │   │   ├── s3_out (1,)
    │   │   ├── s3_top (1,)
    │   │   ├── s3_xc (1,)
    │   │   ├── s3_xs (1,)
    │   │   ├── s3_y (1,)
    │   │   ├── s3_yc (1,)
    │   │   └── s3_ys (1,)
    │   ├── s4
    │   │   │
    │   │   ├── s4_bottom (1,)
    │   │   ├── s4_in (1,)
    │   │   ├── s4_out (1,)
    │   │   ├── s4_top (1,)
    │   │   ├── s4_xc (1,)
    │   │   ├── s4_xs (1,)
    │   │   ├── s4_yc (1,)
    │   │   └── s4_ys (1,)
    │   ├── ss1
    │   │   │
    │   │   ├── ss1_phi (1,)
    │   │   ├── ss1_rx (1,)
    │   │   ├── ss1_rz (1,)
    │   │   ├── ss1_theta (1,)
    │   │   ├── ss1_tx (1,)
    │   │   ├── ss1_tz (1,)
    │   │   ├── ss1_x (1,)
    │   │   ├── ss1_y1 (1,)
    │   │   ├── ss1_y2 (1,)
    │   │   └── ss1_y3 (1,)
    │   ├── ss2
    │   │   │
    │   │   ├── ss2_rx (1,)
    │   │   ├── ss2_theta (1,)
    │   │   ├── ss2_x (1,)
    │   │   ├── ss2_y (1,)
    │   │   └── ss2_z (1,)
    │   ├── t3
    │   │   │
    │   │   ├── t3_m1y (1,)
    │   │   ├── t3_m1z (1,)
    │   │   ├── t3_m2y (1,)
    │   │   ├── t3_m2z (1,)
    │   │   ├── t3_m3rx (1,)
    │   │   ├── t3_m3ry (1,)
    │   │   ├── t3_m3rz (1,)
    │   │   ├── t3_m3y (1,)
    │   │   ├── t3_m3z (1,)
    │   │   ├── t3_m4rx (1,)
    │   │   ├── t3_m4ry (1,)
    │   │   ├── t3_m4x (1,)
    │   │   ├── t3_m4y (1,)
    │   │   └── t3_x (1,)
    │   └── t7
    │       │
    │       ├── t7_m1z (1,)
    │       ├── t7_m2rx (1,)
    │       ├── t7_m2ry (1,)
    │       ├── t7_m2x (1,)
    │       ├── t7_m2y (1,)
    │       ├── t7_m2z (1,)
    │       ├── t7_m3rx (1,)
    │       ├── t7_m3ry (1,)
    │       ├── t7_m3rz (1,)
    │       ├── t7_m3z (1,)
    │       ├── t7_x (1,)
    │       └── t7_y (1,)
    ├── entry_identifier (1,)
    ├── experiment_identifier (1,)
    ├── flyScanDetector
    │   │
    │   ├── Time (1861,)
    │   ├── count_time (1861,)
    │   ├── data (1861, 2160, 2560)
    │   ├── image_key (1861,)
    │   └── zebraSM1 (1861,)
    ├── instrument
    │   │
    │   ├── flyScanDetector
    │   │   │
    │   │   ├── count_time (1861,)
    │   │   └── data (1861, 2160, 2560)
    │   ├── image_key
    │   │   └── image_key (1861,)
    │   ├── name (1,)
    │   ├── source
    │   │   │
    │   │   ├── current (1,)
    │   │   ├── energy (1,)
    │   │   ├── name (1,)
    │   │   ├── probe (1,)
    │   │   └── type (1,)
    │   ├── zebraContinuousMoveController
    │   │   └── Time (1861,)
    │   └── zebraSM1
    │       └── zebraSM1 (1861,)
    ├── program_name (1,)
    ├── scan_command (1,)
    ├── scan_dimensions (1,)
    ├── scan_identifier (1,)
    ├── title (1,)
    ├── tomo_entry
    │   │
    │   ├── control
    │   │   └── data (1,)
    │   ├── data
    │   │   │
    │   │   ├── data (1861, 2160, 2560)
    │   │   └── rotation_angle (1861,)
    │   ├── definition (1,)
    │   ├── instrument
    │   │   │
    │   │   ├── detector
    │   │   │   │
    │   │   │   ├── data (1861, 2160, 2560)
    │   │   │   ├── distance (1,)
    │   │   │   ├── image_key (1861,)
    │   │   │   ├── x_pixel_size (1,)
    │   │   │   └── y_pixel_size (1,)
    │   │   └── source
    │   │       │
    │   │       ├── current (1,)
    │   │       ├── energy (1,)
    │   │       ├── name (1,)
    │   │       ├── probe (1,)
    │   │       └── type (1,)
    │   ├── sample
    │   │   │
    │   │   ├── rotation_angle (1861,)
    │   │   ├── x_translation (1,)
    │   │   ├── y_translation (1,)
    │   │   └── z_translation (1,)
    │   └── title (1,)
    └── user01
        └── username (1,)

```