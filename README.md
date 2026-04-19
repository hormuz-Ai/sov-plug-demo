mkdir policy && cd policy
cat > data_residency.rego << 'EOF'
package data

deny[msg] {
  input.destination_country!= "ZA"
    msg := sprintf("BLOCKED: data attempted to leave South Africa to %v", [input.destination_country])
    }
    EOF
    ./opa eval -d data_residency.rego -i <(echo '{"destination_country":"US"}') "data.deny"