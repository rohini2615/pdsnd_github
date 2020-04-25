### importing libraries
import time
import pandas as pd
import numpy as np
### importing files
 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # cities = ['chicago', 'new york city', 'washington']
    # while inputCity not in cities:
    # print( CITY_DATA.keys())
    inputCity = input_Arg('\nPlease input for city (chicago, new york city, washington)\n',
                 '\nSome Error.Please input for city (chicago, new york city, washington)\n' ,\
                  CITY_DATA.keys())
    # TO DO: get user input for month (all, january, february, ... , june)
    inputMonth = input_Arg('\nPlease input for month (all, january, february, ... , june).\n',\
                 '\nSome Error.Please input for month (all, january, february, ... , june).\n' ,\
                  months)
    # inputMonth = input('\nPlease input for month (all, january, february, ... , june).\n')
    # while inputMonth not in months:
    #     inputMonth = input('\nPlease input for month (all, january, february, ... , june).\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    inputDay = input_Arg('\nPlease input for week (all, monday, tuesday, ... sunday).\n',\
                 '\nSome Input Error.Please input for week (all, monday, tuesday, ... sunday).\n' ,\
                  weekdays)
    # inputDay = input('\nPlease input for day of week (all, monday, tuesday, ... sunday).\n')
    # while inputDay not in weekdays:
    #     inputDay = input('\nPlease input for day of week (all, monday, tuesday, ... sunday).\n')
    print('-'*40)
    return inputCity, inputMonth, inputDay
 
 
def input_Arg(input_print,error_print,enterable_list):
    #inArg = input('\nPlease input for city (chicago, new york city, washington).\n')
    ret = input(input_print).lower().strip()
    while ret not in enterable_list:
        # inArg = input('\nPlease input for city (chicago, new york city, washington).\n')
        ret = input(error_print).lower().strip()
    return ret
 
 
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
 
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
 
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
 
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
 
        # filter by month to create the new dataframe
        df = df[df["month"] == month]
        # print(df)
 
    # filter by day of week if applicable
    if day != 'all':
        # weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        # weekday = weekdays.index(day)
        # print(weekday)
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]
    return df
 
 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
 
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
 
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is:', popular_month)
 
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common popular_day_of_week is:', popular_day_of_week)
 
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour is:', popular_hour)
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
 
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
 
    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most common start_station is:\n', start_station)
 
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most common end_station is:\n', end_station)
 
    # TO DO: display most frequent combination of start station and end station trip
    #print(station.sort('').first())
    #print('The most common station is:\n', df[['Start Station', 'End Station']][df[['Start Station', 'End Station']].duplicated()])
    #print('The most common station is:\n', df[['Start Station','End Station']].count(['Start Station','End Station']))
    # df['Trip'] = df['Start Station'].str.cat(df['End Station'], sep='->')
    #print(df['Trip'])
    # Trip = df['Trip'].mode()[0]
    #print('The most frequent popular trip is:', Trip)
    Trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip is {} to {}".format(Trip[0], Trip[1]))
 
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
 
    # TO DO: display total travel time
    total = df["Trip Duration"].count()
    print("\nTotal duration is:\n",total)
 
    # TO DO: display mean travel time
    df['time'] = pd.to_datetime(df["End Time"]) - df["Start Time"]
    mean_time = df['time'].mean()
    print("\nMean travel time is:\n",mean_time)
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def user_stats(df):
    """Displays statistics on bikeshare users."""
 
    print('\nCalculating User Stats...\n')
    start_time = time.time()
 
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe results of counts of user types is:\n",user_types)
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nThe results of counts of gender is:\n", gender)
    except:
        pass
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common =  df['Birth Year'].mode()[0]
        print("\nearliest of birth is:\n", earliest)
        print("\nmost recent of birth is:\n", recent)
        print("\nmost common year of birth is:\n", common)
    except:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

 
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
 
 
if __name__ == "__main__":
	main()