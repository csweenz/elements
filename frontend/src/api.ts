const BASE_URL = 'http://localhost:8000/api'; // Update this

export const getElementData = async (symbol: string) => {
  try {
    const response = await fetch(`${BASE_URL}/elements/${symbol}`);
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching element data:', error);
    throw error;
  }
};

// Add more API