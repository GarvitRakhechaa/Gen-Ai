import Button from './components/button';

function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Nexus7UI Button Demo</h1>
      <Button style={{ margin: '10px' }}>Click Me</Button>
      <Button disabled style={{ margin: '10px' }}>Disabled Button</Button>
      <Button hoverColor="red" backgroundColor="green" hoverScale={1.2} style={{ margin: '10px' }}>Custom Button</Button>
    </div>
  );
}

export default App;