import movie_search
import requests.exceptions


def main():
    print_header()
    movie_search_query()


def print_header():
    print('------------------------')
    print('   MOVIE SEARCH APP')
    print('------------------------')
    print()


def movie_search_query():
    search = "THIS IS NOT A MOVIE"
    while search.lower().strip() != 'x':
        try:
            search = input('What movie do you want to search for? ')
            if search.lower().strip() != 'x':
                results = movie_search.find_movies(search)
                print('Found {} results for {}.'.format(len(results), search))
                for r in results:
                    print('{}: {}, IMDB Score: {}'.format(r.year, r.title, r.imdb_score))
                    print()

        except ValueError:
            print('Error: Search text is required.')
        except requests.exceptions.ConnectionError:
            print('Error: Internet connection needed.')
        except Exception as x:
            print('Error: Unexpected error: {}.'.format(x))

    print('Exiting, goodbye!')


if __name__ == '__main__':
    main()
