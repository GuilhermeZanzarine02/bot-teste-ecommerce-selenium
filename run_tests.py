import pytest

"""
Executa todos os testes na pasta 'tests' com saída detalhada (-v) e gera um relatório HTML em 'reports/report.html'
"""

pytest.main([
    "-v",                            
    "--html=reports/report.html",  
    "--self-contained-html",       
    "testes/"                       
])
