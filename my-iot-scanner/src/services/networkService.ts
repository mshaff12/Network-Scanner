import axios from 'axios';

const BASE_URL = 'http://localhost:5000'; // Replace with the appropriate URL of your Python server

// Function to initiate the network scanning process
export const scanNetwork = async (): Promise<string[]> => {
  try {
    const response = await axios.post(`${BASE_URL}/scan`);

    if (response.status === 200) {
      return response.data.devices;
    } else {
      throw new Error('Network scan failed');
    }
  } catch (error) {
    throw new Error('Network scan failed');
  }
};

// Function to initiate the vulnerability assessment for a device
export const assessDevice = async (device: string): Promise<string[]> => {
  try {
    const response = await axios.post(`${BASE_URL}/assess`, { device });

    if (response.status === 200) {
      return response.data.vulnerabilities;
    } else {
      throw new Error('Device assessment failed');
    }
  } catch (error) {
    throw new Error('Device assessment failed');
  }
};
