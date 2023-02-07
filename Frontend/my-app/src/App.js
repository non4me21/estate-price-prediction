import React, { useReducer, useState } from 'react';
import './App.css';

const formReducer = (state, event) => {
  return {
    ...state,
    [event.name] : event.value
  }
}

async function getPrice(url) {
  const response = await fetch(url);
  return response
}

function App() {
  const [data, setData] = useReducer(formReducer, {});
  const [submitted, setSubmitted] = useState(false);
  const [price, setPrice] = useState(0);
  
  const handleSubmit = event => {
    event.preventDefault();
    setSubmitted(true)
    if (Object.values(data).filter(n => n).length > 2) {
      if (data.area > 0) {
        const params = new URLSearchParams({
        address: data.address,
        area: data.area,
        rooms: data.rooms
      });
      const url = 'http://localhost:8080/pricing/'.concat('?', params.toString())
      getPrice(url).then((response) => response.json()).then((data) => {setPrice(data.price);});
      setSubmitted(false)
    }
  }
    
  }

  const handleChange = event => {
    setData({
      name: event.target.name,
      value: event.target.value,
    })
  }
  return (
    <div className='main'>
    <div className='wrapper'>
      <h1>Kalkulator ceny mieszkania</h1>
      {Object.values(data).filter(n => n).length < 3 && submitted &&
      <div name="emptyText" className='warning'>Uzupełnij wszystkie pola</div>}
      <form onSubmit={handleSubmit}>
        <fieldset className='textInput'>
          <label> 
            <p>Adres:</p>
            <input name='address' onChange={handleChange} placeholder='np.: Wrocław, Zakładowa'/>
          </label>
        </fieldset>
        <fieldset className='textInput'>
          <label> 
            <p>Metraz:</p>
            <input name='area' onChange={handleChange} placeholder='np.: 76.5'/>
          </label>
        </fieldset>
        {data.area < 1 && <div id='minusArea' className='warning'>Metraz nie moze byc ujemny</div>}
        <fieldset className='selectInput'>
          <label>
            <p>Pokoje:</p>
            <select name='rooms' onChange={handleChange}>
              <option value="">Wybierz liczbę pokoi</option>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
              <option value="6">6</option>
              <option value="7">7</option>
              <option value="8+">8</option>
            </select>
          </label>
        </fieldset>
        <button name='submit' type="submit">Oblicz</button>
      </form>
      {price > 0 &&
      <div className='priceInfo'>Szacowana cena mieszkania:
        <div>{price}zł</div>
        </div>
      }
    <div className='footer'>made by walega</div>
    </div>
    </div>
  );
}

export default App;
