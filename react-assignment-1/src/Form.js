import React, { useState } from 'react';

function Form() {
  const [text, setText] = useState('');
  const [count, setCount] = useState('');
  const [output, setOutput] = useState('');

  function handleSubmit(event) {
    event.preventDefault();
    if (!text.trim() || isNaN(count) || count < 1) {
      alert('Please enter a valid string and a positive integer');
      return;
    }
    setOutput(text.repeat(count));
  }

  return (
    <form onSubmit={handleSubmit}>
        <div>
            <label>
                String:
                <input type="text" value={text} onChange={(e) => setText(e.target.value)} />
            </label>
        </div>
      <div>
        <label>
            Number:
            <input type="number" value={count} onChange={(e) => setCount(e.target.value)} />
        </label>
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
      
      {output && <p>{output}</p>}
    </form>
  );
}

export default Form;
