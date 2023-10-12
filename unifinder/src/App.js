import React, { Component, useEffect, useState } from 'react';
import axios from 'axios';

class App extends Component {
    state = {
        data: {}
    };

    componentDidMount() {
        axios.get('/api/data/')
            .then(response => {
                this.setState({ data: response.data });
            })
            .catch(error => {
                console.error(error);
            });
    }

    render() {
        return (
            <div>
                <h1>{this.state.data.message}</h1>
            </div>
        );
    }
}

export default App;






