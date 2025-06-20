fn main() -> Result<(), Box<dyn std::error::Error>> {
    let google_include = "C:/protoc/include"; // Adjust this path!

    tonic_build::configure()
        .build_client(true)
        .build_server(true)
        .compile(&["proto/greet.proto"], &["proto", google_include])?;
    Ok(())
}