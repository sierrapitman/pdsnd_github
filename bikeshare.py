{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "667f7d04",
   "metadata": {},
   "outputs": [],
   "source": [
    "##### Final Project! ######\n",
    "\n",
    "import time\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import datetime\n",
    "\n",
    "CITY_DATA = { 'chicago': 'chicago.csv',\n",
    "              'new york city': 'new_york_city.csv',\n",
    "              'washington': 'washington.csv' }\n",
    "\n",
    "cities = ['chicago', 'new york city', 'washington']\n",
    "months = ['all','january','february','march','april','may','june']\n",
    "days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']\n",
    "\n",
    "def get_filters():\n",
    "    \"\"\"\n",
    "    Asks user to specify a city, month, and day to analyze.\n",
    "\n",
    "    Returns:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    \"\"\"\n",
    "    print('Hello! Let\\'s explore some US bikeshare data!')\n",
    "    \n",
    "    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs\n",
    "    while True:\n",
    "        #cities = ['chicago', 'new york city', 'washington']\n",
    "        city = input('\\nPlease select a city: Chicago, New York City, Washington: \\n').lower()\n",
    "        try:\n",
    "            if cities.index(city)>=0:\n",
    "                print(f'\\nYou have chosen to analyze {city.title()}!\\n')\n",
    "                break\n",
    "        except ValueError:\n",
    "            print(f'\\n\"{city}\" invalid. Please try again.\\n')\n",
    "            \n",
    "    # get user input for month (all, january, february, ... , june)\n",
    "    while True:\n",
    "        #months = ['all','january','february','march','april','may','june']\n",
    "        month = input('\\nPlease select a month: January, February, March, April, May, June, or all:\\n').lower()\n",
    "        try:\n",
    "            if months.index(month)>=0:\n",
    "                print(f'\\nYou have chosen to analyze {month.title()}!\\n')\n",
    "                break\n",
    "        except ValueError:\n",
    "            print(f'\\n\"{month}\" invalid. invalid. Please try again.\\n')\n",
    "            \n",
    "    # get user input for day of week (all, monday, tuesday, ... sunday)\n",
    "    while True:\n",
    "        #days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']\n",
    "        day = input('\\nPlease select a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all:\\n').lower()\n",
    "        try:\n",
    "            if days.index(day)>=0:\n",
    "                print(f'\\nYou have chosen to analyze {day.title()}!\\n')\n",
    "                break\n",
    "        except ValueError:\n",
    "            print(f'\\n\"{day}\" invalid. Please try again.\\n')\n",
    "\n",
    "    print('-'*40)\n",
    "    return city, month, day\n",
    "\n",
    "\n",
    "def load_data(city, month, day):\n",
    "    \"\"\"\n",
    "    Loads data for the specified city and filters by month and day if applicable.\n",
    "\n",
    "    Args:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    Returns:\n",
    "        df - Pandas DataFrame containing city data filtered by month and day\n",
    "    \"\"\"\n",
    "    #loads city data\n",
    "    print(\"\\nLoading data. Please hold...\")\n",
    "    df = pd.read_csv(CITY_DATA[city])\n",
    "\n",
    "    #convert Start Time to datetime format\n",
    "    df['Start Time'] = pd.to_datetime(df['Start Time'])\n",
    "    \n",
    "    #convert End Time to datetime format\n",
    "    df['End Time'] = pd.to_datetime(df['End Time'])\n",
    "    \n",
    "    #create new columns for month columns\n",
    "    df['month'] = df['Start Time'].dt.month\n",
    "    df['month_name'] = df['Start Time'].dt.month_name()\n",
    "    \n",
    "    #create new columns for day columns\n",
    "    df['weekday'] = df['Start Time'].dt.dayofweek\n",
    "    df['weekday_name'] = df['Start Time'].dt.dayofweek.replace({0:'monday', 1:'tuesday', 2:'wednesday', 3: 'thursday', 4:'friday', 5:'saturday', 6:'sunday'})\n",
    "    \n",
    "    #create new hour column\n",
    "    df['hour'] = df['Start Time'].dt.hour\n",
    "    \n",
    "    #create roundtrip column\n",
    "    df['roundtrip'] = df['Start Station'] + \" to \" + df['End Station']\n",
    "        \n",
    "    # filter by month to create the new dataframe\n",
    "    if month != 'all':\n",
    "        df = df.loc[df['month_name'] == month.title()]\n",
    "    \n",
    "    #filter by day to create the enw dataframe\n",
    "    if day != 'all':\n",
    "        df = df.loc[df['weekday_name'] == day.lower()]\n",
    "    \n",
    "    return df\n",
    "\n",
    "\n",
    "def time_stats(df):\n",
    "    \"\"\"Displays statistics on the most frequent times of travel.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Frequent Times of Travel...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # display the most common month\n",
    "    common_month = df['month_name'].mode()[0]\n",
    "    print(f'\\nThe most common month is {common_month}.')\n",
    "      \n",
    "    # display the most common day of week\n",
    "    common_day = df['weekday_name'].mode()[0]\n",
    "    print(f'\\nThe most common day is {common_day}.')\n",
    "      \n",
    "    # display the most common start hour\n",
    "    common_hour = df['hour'].mode()[0]\n",
    "    print(f'\\nThe most common start hour is {common_hour}.')\n",
    "      \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def station_stats(df):\n",
    "    \"\"\"Displays statistics on the most popular stations and trip.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Popular Stations and Trip...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # display most commonly used start station\n",
    "    common_start_station = df['Start Station'].mode()[0]\n",
    "    print(f'\\nThe most common Start Station is {common_start_station}.')\n",
    "    \n",
    "    # display most commonly used end station\n",
    "    common_end_station = df['End Station'].mode()[0]\n",
    "    print(f'\\nThe most common End Station is {common_end_station}.')\n",
    "      \n",
    "    # display most frequent combination of start station and end station trip\n",
    "    common_roundtrip = df['roundtrip'].mode()[0]\n",
    "    print(f'\\nThe most common Roundtrip is {common_roundtrip}.')\n",
    "      \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def trip_duration_stats(df):\n",
    "    \"\"\"Displays statistics on the total and average trip duration.\"\"\"\n",
    "\n",
    "    print('\\nCalculating Trip Duration...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # display total travel time\n",
    "    total_trip_duration = df['Trip Duration'].sum()\n",
    "    print(f'\\nThe total trip time in minutes is {total_trip_duration}.')\n",
    "    \n",
    "    # display mean travel time\n",
    "    mean_travel_time = df['Trip Duration'].mean()\n",
    "    print(f'\\nThe average trip time in minutes is {mean_travel_time}.')\n",
    "    \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def user_stats(df):\n",
    "    \"\"\"Displays statistics on bikeshare users.\"\"\"\n",
    "\n",
    "    print('\\nCalculating User Stats...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # Display counts of user types\n",
    "    user_type_counts = df['User Type'].value_counts()\n",
    "    print(user_type_counts.to_frame())\n",
    " \n",
    "    # Display counts of gender\n",
    "    if \"Gender\" in df.columns:\n",
    "        gender_counts = df['Gender'].value_counts()\n",
    "        print(gender_counts.to_frame())\n",
    "\n",
    "    if \"Birth Year\" in df.columns:\n",
    "        # Display earliest, most recent, and most common year of birth\n",
    "        min_birth_year = int(df['Birth Year'].min())\n",
    "        print(f'\\nThe minimum birth year is {min_birth_year}.')   \n",
    "\n",
    "        max_birth_year = int(df['Birth Year'].max()) \n",
    "        print(f'\\nThe maximum birth year is {max_birth_year}.')    \n",
    "\n",
    "        common_birth_year = int(df['Birth Year'].mode())\n",
    "        print(f'\\nThe most common birth year is {common_birth_year}.')    \n",
    "    \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "#add option to see 5 rows\n",
    "#alternative code provided by Udacity is listed below"
    "def view_head(df):\n",
    "    while True:\n",
    "        input_option = input(\"Would you like to view 5 rows of data? yes or no:\\n\").lower()\n",
    "        if input_option != 'yes':\n",
    "            break \n",
    "        else:\n",
    "            print(df.iloc[:5])\n",
    "            \n",
    "\"\"\"UDACITY suggestion for view_head option\n",
    "def display_raw_data(df):\n",
    "    \"\"\" 'Your docstring here' \"\"\"\n",
    "    i = 0\n",
    "    raw = input(\"\\nWould you like to see first 5 rows of raw data; type 'yes' or 'no'?\\n\").lower()\n",
    "    pd.set_option('display.max_columns',200)\n",
    "\n",
    "    while True:            \n",
    "        if raw == 'no':\n",
    "            break\n",
    "        elif raw == 'yes':\n",
    "            print(df[i:i+5]) \n",
    "            raw = input(\"\\nWould you like to see next rows of raw data?\\n\").lower() \n",
    "            i += 5\n",
    "        else:\n",
    "            raw = input(\"\\nYour input is invalid. Please enter only 'yes' or 'no'\\n\").lower()\n",
    "\"\"\"            \n",
    "    \n",
    "def main():\n",
    "    while True:\n",
    "        city, month, day = get_filters()\n",
    "        df = load_data(city, month, day)\n",
    "        time_stats(df)\n",
    "        station_stats(df)\n",
    "        trip_duration_stats(df)\n",
    "        user_stats(df)\n",
    "        view_head(df)\n",
    "        restart = input('\\nWould you like to restart? Enter yes or no.\\n')\n",
    "        if restart.lower() != 'yes':\n",
    "            break\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
