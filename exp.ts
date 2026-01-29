// Movie related interfaces
export interface Movie {
  id: string;
  title: string;
  releaseYear: number;
  genrea: string[];
  rating: number;
  director: string;
  cast: string[];
  duration: number; // in minutes
  description: string;
  posterUrl?: string;   
  trailerUrl?: string;
}

export interface MovieSearchFilters {
  title?: string;
  genre?: string[];
  minRating?: number;
  releaseYear?: number;
  director?: string;
  actor?: string;
}

export interface IMovieService {
  getMovieById(id: string): Promise<Movie | null>;
  searchMovies(filters: MovieSearchFilters): Promise<Movie[]>;
}



// User related interfaces
export interface User {
  id: string;
  username: string;
  email: string;
  watchlist: string[]; // Array of movie IDs
  preferences: {
    favoriteGenres: string[];
    notificationEnabled: boolean;
  };
  createdAt: Date;
  updatedAt: Date;
}

// Dummy data generator functions
export function generateDummyMovie(id: string): Movie {
  const genres = [
    'Action', 'Comedy', 'Drama', 'Horror', 
    'Sci-Fi', 'Thriller', 'Romance', 'Documentary'
  ];
  
  const firstNames = ['John', 'Jane', 'Robert', 'Emily', 'Michael', 'Sarah', 'David', 'Emma'];
  
  const randomName = () => 
    `${firstNames[Math.floor(Math.random() * firstNames.length)]}`;
    
  return {
    id,
    title: `Movie ${Math.floor(Math.random() * 1000)}`,
    releaseYear: 2000 + Math.floor(Math.random() * 25),
    genrea: [
      genres[Math.floor(Math.random() * genres.length)],
      genres[Math.floor(Math.random() * genres.length)]
    ].filter((v, i, a) => a.indexOf(v) === i), // Remove duplicates
    rating: Number((Math.random() * 5).toFixed(1)),
    director: randomName(),
    cast: Array(3).fill(0).map(() => randomName()),
    duration: 80 + Math.floor(Math.random() * 100),
    description: 'This is a dummy movie description. It would contain a brief summary of the movie plot and main characters.',
    posterUrl: `https://example.com/posters/${id}.jpg`,
    trailerUrl: `https://example.com/trailers/${id}`
  };
}

// Dummy API functions
export async function searchMovies(filters: MovieSearchFilters): Promise<Movie[]> {
  // Simulate API call delay
  await new Promise(resolve => setTimeout(resolve, 500));
  
  // In a real implementation, this would query a database
  const dummyMovies = Array(10).fill(0).map((_, i) => 
    generateDummyMovie(`mv-${Date.now()}-${i}`)
  );
  
  // Apply filters (simplified)
  return dummyMovies.filter(movie => {
    if (filters.title && !movie.title.toLowerCase().includes(filters.title.toLowerCase())) {
      return false;
    }
    if (filters.genre && !filters.genre.some(g => movie.genrea.includes(g))) {
      return false;
    }
    if (filters.minRating && movie.rating < filters.minRating) {
      return false;
    }
    if (filters.releaseYear && movie.releaseYear !== filters.releaseYear) {
      return false;
    }
    if (filters.director && !movie.director.toLowerCase().includes(filters.director.toLowerCase())) {
      return false;
    }
    if (filters.actor && !movie.cast.some(actor => 
      actor.toLowerCase().includes(filters.actor!.toLowerCase())
    )) {
      return false;
    }
    return true;
  });
}

export async function getMovieById(id: string): Promise<Movie | null> {
  // Simulate API call delay
  await new Promise(resolve => setTimeout(resolve, 300));
  
  // In a real implementation, this would query a database
  return generateDummyMovie(id);
}

// Example usage:
/*
async function exampleUsage() {
  // Search for action movies
  const actionMovies = await searchMovies({
    genre: ['Action'],
    minRating: 4.0
  });
  
  console.log('Action movies:', actionMovies);
  
  // Get a specific movie
  const movie = await getMovieById('mv-123');
  console.log('Movie details:', movie);
}
*/
