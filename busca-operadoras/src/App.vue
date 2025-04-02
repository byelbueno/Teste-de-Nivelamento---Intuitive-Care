<template>
  <div id="app">
    <header class="header">
      <h1>Busca de Operadoras</h1>
    </header>

    <main class="main-content">
      <div class="search-box">
        <input
          type="text"
          v-model="termo"
          placeholder="Digite o nome ou termo relacionado"
          class="search-input"
        />
        <button @click="buscarOperadoras" class="search-button">Buscar</button>
      </div>

      <div v-if="operadoras.length" class="results">
        <h2>Resultados Encontrados:</h2>
        <ul class="operadoras-list">
          <li v-for="operadora in operadoras" :key="operadora.razao_social" class="operadora-item">
            <strong>{{ operadora.razao_social }}</strong>
            <p>
              Nome Fantasia: {{ operadora.nome_fantasia || 'Sem Nome Fantasia' }}<br />
              Modalidade: {{ operadora.modalidade }}<br />
              Localização: {{ operadora.cidade }}/{{ operadora.uf }}
            </p>
          </li>
        </ul>
      </div>

      <p v-else class="no-results">Nenhuma operadora encontrada.</p>
    </main>

    <footer class="footer">
      <p>&copy; 2025 Busca de Operadoras. Todos os direitos reservados.</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      termo: "",
      operadoras: [],
    };
  },
  methods: {
    async buscarOperadoras() {
      try {
        const response = await axios.get("http://localhost:5000/buscar-operadoras", {
          params: { termo: this.termo },
        });
        this.operadoras = response.data;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
      }
    },
  },
};
</script>

<style>
body {
  margin: 0;
  font-family: "Arial", sans-serif;
  background-color: #f7f7f9;
  color: #333;
}

.header {
  background-color: #6a1b9a;
  color: white;
  padding: 20px;
  text-align: center;
}

.main-content {
  padding: 20px;
}

/* Caixa de busca */
.search-box {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.search-input {
  width: 300px;
  padding: 10px;
  border-radius: 5px;
  border: none;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 2px 4px;
}

.search-button {
  background-color: #6a1b9a;
  color: white;
  border: none;
  padding: 10px 15px;
  margin-left: 10px;
  border-radius: 5px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #4a148c;
}

/* Resultados */
.results h2 {
  text-align: center;
}

.operadoras-list {
  list-style-type: none;
  padding: 0;
}

.operadora-item {
  background-color: white;
  border-radius: 5px;
  box-shadow: rgba(0,0,0,0.1) 0px 2px 4px;
  margin-bottom: 15px;
  padding: 15px;
}

.no-results {
  text-align: center;
}

.footer {
  background-color: #6a1b9a;
  color: white;
  text-align: center;
}
</style>
