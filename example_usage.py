from client import AutonomousLegalContractClauseSynthesizerClient

def main():
    client = AutonomousLegalContractClauseSynthesizerClient()
    res = client.synthesize_contract_agreement('MUTUAL_NON_DISCLOSURE_AGREEMENT', 'DELAWARE_USA', 5, 1.0)
    print('Contract Synthesizer: ' + res['contract_id'] + ' (' + res['agreement_type'] + ')')
    print('Jurisdiction: ' + res['jurisdiction'] + ' | Clauses: ' + str(res['clauses_structured_count']))
    print('Compliance Score: ' + str(res['statutory_compliance_score_pct']) + '% | Risk: ' + res['risk_exposure_grade'])
    print('Contract URL: ' + res['contract_markdown_url'])

if __name__ == '__main__':
    main()
