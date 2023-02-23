Build a zemax merit function.

If you have a lens power profile, write it in CSV format. The first column is the distance to the center of the lens, the second column is the diopter, and don't have the header.

This program will generate the corresponding zemax merit function.
There are several parts included.

* FTGT, FTLT, used to constrain the thickness of the lens
* POWP, used to constrain the diopter of the lens in different positions
* DIFF, DIVB, used to calculate the first-order derivative of the refractive power to avoid too pronounced local sudden changes.

You can use on Streamlit: 
https://goldengrape-zemax-merit-function-builder-streamlit-app-lyt845.streamlit.app/