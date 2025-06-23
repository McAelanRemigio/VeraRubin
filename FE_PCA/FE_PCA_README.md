{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b6fc5acb-d552-4a1e-9f12-4ab8d8d6443a",
   "metadata": {},
   "source": [
    "# CURRENTLY IN PROGRESS\n",
    "\n",
    "FEATURE ENGINEERING\n",
    "\n",
    "Features \n",
    "1. ra – Sky position (horizontal)\n",
    "2. Decl – Sky position (vertical)\n",
    "3. fluxChi2 – Measure of variability strength\n",
    "4. fluxSigma – Standard deviation of brightness\n",
    "5. fluxStetsonJ – Variability index (J)\n",
    "6. fluxStetsonK – Variability index (K)\n",
    "7. fluxMax – Maximum brightness\n",
    "8. fluxMin – Minimum brightness\n",
    "9. fluxMAD – Robust variability measure\n",
    "10. fluxSkew – Light curve asymmetry\n",
    "11. maxSlope – Fastest brightness change\n",
    "12. linearSlope – Overall trend in brightness\n",
    "13. Counts – Number of observations\n",
    "14. g-r – Color: green minus red\n",
    "15. R-i – Color: red minus infrared\n",
    "16. G-i – Color: green minus infrared\n",
    "17. cModelFlux – Total brightness (extended sources)\n",
    "18. psfFlux – Brightness for point sources\n",
    "19. calib_psfFlux – Calibrated brightness\n",
    "20. extendedness – Point vs. extended source\n",
    "21. deblendedPSF – Quality of brightness measure\n",
    "22. footprintArea – Size of object in the sky\n",
    "\n",
    "\n",
    "Good news, holy shit we're able to clear up that much data to just 22 columns worth of data. This will be good for when we build our ML classification model which will most likely be a neural network. \n",
    "\n",
    "Bad ish news, it might be too many features? We'll use this section to try and get rid of as many not so correlated features so that we can save more time computationally given our time constraint. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94c4e305-b23f-444f-aa82-a849a43f2c57",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "LSST",
   "language": "python",
   "name": "lsst"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
