const prod = {
    url: {
        API_URL: 'https://hardwareresources12.herokuapp.com',
    }
};

const dev = {
    url: {
        API_URL: 'http://localhost:5000'
    }
};

export const config = process.env.NODE_ENV === 'development' ? dev : prod;