{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Analiza danych z Firebase\n",
    "\n",
    "Ten notebook pokazuje, jak pracować z danymi z Firebase, wizualizować je i analizować."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "import sys\n",
    "sys.path.append('..')\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from datetime import datetime, timedelta\n",
    "\n",
    "from src.database import FirebaseManager\n",
    "\n",
    "%matplotlib inline\n",
    "plt.style.use('seaborn')\n",
    "sns.set_palette('husl')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Połączenie z bazą danych"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "from dotenv import load_dotenv\n",
    "import os\n",
    "\n",
    "load_dotenv()\n",
    "firebase = FirebaseManager(os.getenv('FIREBASE_CREDENTIALS_PATH'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Pobieranie i analiza danych\n",
    "\n",
    "Pobierzmy dane użytkowników i przekształćmy je do DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Pobierz wszystkich użytkowników 25+\n",
    "users_data = firebase.query_collection('users', 'age', '>=', 25)\n",
    "\n",
    "# Konwersja do DataFrame\n",
    "df_users = pd.DataFrame(users_data)\n",
    "df_users.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Wizualizacja danych\n",
    "\n",
    "Stwórzmy kilka wykresów pokazujących rozkład wieku i umiejętności"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Rozkład wieku\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.histplot(data=df_users, x='age', bins=20)\n",
    "plt.title('Rozkład wieku użytkowników')\n",
    "plt.xlabel('Wiek')\n",
    "plt.ylabel('Liczba użytkowników')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Analiza umiejętności\n",
    "skills_count = df_users['skills'].explode().value_counts()\n",
    "\n",
    "plt.figure(figsize=(12, 6))\n",
    "skills_count.plot(kind='bar')\n",
    "plt.title('Najpopularniejsze umiejętności')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Zapisywanie wyników analizy\n",
    "\n",
    "Możemy zapisać wyniki naszej analizy z powrotem do Firebase"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Przygotuj statystyki\n",
    "stats = {\n",
    "    'avg_age': float(df_users['age'].mean()),\n",
    "    'most_common_skills': skills_count.head(5).to_dict(),\n",
    "    'total_users': len(df_users),\n",
    "    'analysis_date': datetime.now().isoformat()\n",
    "}\n",
    "\n",
    "# Zapisz do Firebase\n",
    "firebase.add_data('analytics', f'user_stats_{datetime.now().strftime(\"%Y%m%d\")}', stats)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11.0"
  }
 }
}
