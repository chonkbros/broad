{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "801b50a4-f647-4813-80a3-87f032a37e84",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e2ec4db5-2f32-41c5-8ba7-25f2e9db103a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# API endpoint\n",
    "url = \"https://api-v3.mbta.com/routes\"\n",
    "\n",
    "# Query parameters\n",
    "params = {\n",
    "    \"filter[type]\": \"0,1\"\n",
    "}\n",
    "\n",
    "# Make the GET request\n",
    "response_1 = requests.get(url, params=params)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "00ce6fc3-e2a5-4bf9-9990-cbe8554ae389",
   "metadata": {},
   "outputs": [],
   "source": [
    "response_1 = response_1.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "fc983e5a-c29c-4c5c-a540-eeb05a9bef07",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/tmp/ipykernel_50568/71989386.py:2: FutureWarning: Returning a DataFrame from Series.apply when the supplied function returns a Series is deprecated and will be removed in a future version.\n",
      "  df_attributes = df['attributes'].apply(pd.Series)\n"
     ]
    }
   ],
   "source": [
    "df = pd.DataFrame(response_1['data'])\n",
    "df_attributes = df['attributes'].apply(pd.Series)\n",
    "names = df_attributes['long_name']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b47743c-79e5-43c1-8b02-7d1f0e37ca4f",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(names)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
