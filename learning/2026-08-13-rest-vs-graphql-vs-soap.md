# Day 1: REST vs GraphQL vs SOAP

> **Track:** API & Web  
> **Date:** 2026-08-13  
> **Estimated time:** 45–60 minutes

## Why this matters

Compare resource-oriented REST, query-driven GraphQL, and contract-heavy SOAP. Understand request and response shapes, schemas, caching, and error handling.

This choice affects client complexity, network usage, observability, integration contracts, and long-term maintenance.

## Core comparison

| Aspect | REST | GraphQL | SOAP |
|---|---|---|---|
| Main model | Resources and HTTP endpoints | Client-defined queries over a typed schema | Operations defined by a strict service contract |
| Common payload | JSON | JSON | XML |
| Contract | Often OpenAPI | GraphQL schema | WSDL |
| Fetching data | Server defines each response | Client requests exact fields | Operation defines a fixed message |
| HTTP caching | Natural with URLs and methods | Requires more deliberate handling | Usually handled outside normal HTTP caching |
| Error style | HTTP status codes plus response body | Often HTTP 200 with an `errors` field | SOAP Fault |
| Strong fit | Public CRUD APIs and web services | Complex UIs with varied data needs | Enterprise integrations requiring strict standards |

## Decision guide

Choose **REST** when:

- Resources map naturally to URLs.
- Standard HTTP behavior and caching matter.
- You want a simple API that many clients can consume.

Choose **GraphQL** when:

- Different clients need different combinations of related data.
- Over-fetching or multiple round trips create a real problem.
- Your team can operate schema governance, query limits, and resolver performance.

Choose **SOAP** when:

- An enterprise integration requires WSDL or WS-* standards.
- Strict contracts, formal faults, and established tooling matter.
- You must integrate with a system that already exposes SOAP.

## Learning plan

1. **Understand, 15 minutes**  
   Explain resource-oriented, query-driven, and contract-driven APIs in your own words.

2. **Compare, 10 minutes**  
   Review how each approach handles contracts, errors, caching, and client flexibility.

3. **Build, 20 minutes**  
   Design the same movie-search operation in all three styles.

4. **Verify, 5 minutes**  
   Answer the checkpoint without reopening this note.

## Practical task

Model a request for a movie with its title, genres, and three latest reviews.

### REST

```http
GET /movies/42
GET /movies/42/reviews?limit=3
```

Consider whether embedding reviews or creating a dedicated endpoint is cleaner.

### GraphQL

```graphql
query {
  movie(id: "42") {
    title
    genres
    reviews(limit: 3) {
      rating
      comment
    }
  }
}
```

Notice how the client selects the response shape.

### SOAP

Sketch a `GetMovieDetails` operation with a typed request, typed response, and possible `MovieNotFoundFault`.

### Definition of done

- [ ] I can explain REST, GraphQL, and SOAP without reading definitions.
- [ ] I can identify one appropriate use case for each.
- [ ] I can explain why GraphQL does not automatically solve slow APIs.
- [ ] I completed the movie-search design.
- [ ] I wrote one remaining question.

## Checkpoint

1. Why can GraphQL reduce over-fetching but still create expensive server queries?
2. Why does REST usually integrate more naturally with HTTP caching?
3. What does WSDL provide in a SOAP service?
4. Which approach would you choose for a simple public CRUD API, and why?

## Personal notes

- Key insight:
- Example:
- Remaining question:

## Next topic

**HTTP methods and idempotency**, in the **API & Web** track.
